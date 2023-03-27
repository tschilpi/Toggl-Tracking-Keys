import streamlit as st
import record_hotkeys
import check_hotkeys
import config
import main_test


def initialize_session_state():
    # Initialize session state with default values.
    state_defaults = {
        'submit_check': False,
        'check': False,
        'start_check': False,
        'button_text': "Click to activate hotkeys",
        'button_texts': ["Click to record hotkey"] * 3,
        'hotkeys': ['placeholder'] + [None] * 2,
        'listener': "placeholder",
        'hotkey_values': [1, 2, 3],
        'project_values': ["Default"] * 3,
        'enddata': None
    }

    for key, default_value in state_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

initialize_session_state()

# # connect to API with environment variable
# if 'enddata' not in st.session_state:
#     results = main_test.fetch_user_data()
#     if results is None:
#         st.error('Could not fetch API data.', icon="🚨")
#     else:
#         st.session_state.enddata = results

def get_project_lists():
    # Get project lists, project IDs, and a dictionary mapping IDs to names.
    project_list = []
    project_ids = []

    for element in st.session_state.enddata:
        project_list.append(element['name'])
        project_ids.append(element['id'])

    id_to_name = {id: name for id, name in zip(project_list, project_ids)}

    return project_list, project_ids, id_to_name


def main():


    st.title('Global Hotkeys for Toggl :sunglasses:')
    st.write('')
    st.write('')

    col1, col2, _ = st.columns([1,1,1])
    project_list, project_ids, id_to_name = get_project_lists()

    def record_hotkey(index):
        # Record hotkey, update the button text and store the hotkey value in session state.

        recorded_key = record_hotkeys.main()
        st.session_state['button_texts'][index - 1] = recorded_key

        fset = frozenset(record_hotkeys.COMBINATIONS[0])
        st.session_state['hotkey_values'][index] = fset

        record_hotkeys.COMBINATIONS.clear()

    def display_record_hotkey_buttons():
        # Display the hotkey record buttons in the Streamlit UI.
        with col1:
            for index in range(3):
                st.write(f'Hotkey {index+1}')
                hotkey_button = st.button(
                    st.session_state['button_texts'][index - 1],
                    on_click=(lambda index=index: record_hotkey(index)),
                    key=f'button_{index + 2}',
                    disabled=st.session_state.check,
                    )

    display_record_hotkey_buttons()

    # Display the select boxes for project selection in the Streamlit UI.
    with col2:
        for index in range(3):
            st.write(f"Select project for Hotkey {index + 1}")
            option = st.selectbox(
                f"Select your project for Hotkey {index + 1}",
                (project_list),
                label_visibility="collapsed",
                index=index + 1,
                key=f'selectbox{index + 1}',
                disabled=st.session_state.check,
            )

            selected_id = id_to_name[option]
            st.session_state.project_values[index] = selected_id

    ## Check for all edge cases
    # Edge case 1: non-unique hotkeys chosen
    if len(set(st.session_state['hotkey_values'])) < 3:
        st.write('')
        st.error('You must choose unique hotkeys.', icon="🚨")
        st.session_state.start_check = True

    # Edge case 2: non-unique projects chosen
    elif len(set(st.session_state['project_values'])) < 3:
        st.write('')
        st.error('You must choose unique projects.', icon="🚨")
        st.session_state.start_check = True

    # Edge case 3: no hotkey has been recorded yet
    elif all(bt == "Click to record hotkey" for bt in st.session_state['button_texts']):
        st.session_state.start_check = True
    else:
        st.session_state.start_check = False

    def change_state():
        # Toggle the hotkey activation state and start or stop the hotkey listener.
        if st.session_state['button'] and not st.session_state.check:
            st.session_state.button_text = "Hotkeys activated. Click to deactivate."
            st.session_state.check = True

            # make sure to only activate hotkeys if they have been set
            hotkeylist = []
            for index, hotkey_value in enumerate(st.session_state.hotkey_values):
                if hotkey_value != index + 1:
                    hotkeylist.append((hotkey_value, st.session_state.project_values[index]))

            listener = check_hotkeys.execute_hotkeys(hotkeylist)
            st.session_state.listener = listener

        elif st.session_state['button'] and st.session_state.check:
            st.session_state.button_text = "Hotkeys deactivated. Click to activate."
            st.session_state.check = False

            st.session_state.listener.stop()


    st.write('')
    st.write('')

    first_button = st.button(st.session_state.button_text, on_click=change_state, key='button', disabled=st.session_state.start_check)


#Render the UI for API authentication
placeholder = st.empty()

if st.session_state.enddata is None:
    with placeholder.form('Default', clear_on_submit=True):
        st.title('Global Hotkeys for Toggl :sunglasses:')
        st.write("")
        input = st.text_input('Please input the name of your environment variable set to the toggl API key to authenticate.', key=10)
        submitted = st.form_submit_button()
        if submitted:
            config.update_env_variable(input)
            results = main_test.fetch_user_data()
            if results is None:
                st.error('Could not fetch API data.', icon="🚨")
            else:
                st.session_state.enddata = results
                placeholder.empty()

#If authentication was successful: Start main app
if st.session_state.enddata is not None:
    main()
