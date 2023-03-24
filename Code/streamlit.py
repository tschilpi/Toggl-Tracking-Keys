import streamlit as st
from pynput import keyboard as pynputkeys
import scratch
import hotkeys_finalversion
import config
import requests
import json
from base64 import b64encode
import main_test
import subprocess


if 'submit_check' not in st.session_state:
    st.session_state.submit_check = False

if 'enddata' not in st.session_state:
    results = main_test.fetch_user_data()
    if results is None:
        st.error('Could not fetch API data.', icon="🚨")
    else:
        st.session_state.enddata = results



st.title('Global Hotkeys for Toggl :sunglasses:')
st.write('')
st.write('')


def main(enddata):
    if 'check' not in st.session_state:
        st.session_state.check = False

    if 'start_check' not in st.session_state:
        st.session_state.start_check = False

    if 'button_text' not in st.session_state:
        st.session_state.button_text = "Click to activate hotkeys"

    if 'button_text2' not in st.session_state:
        st.session_state.button_text2 = "Click to record hotkey"

    if 'button_text3' not in st.session_state:
        st.session_state.button_text3 = "Click to record hotkey"

    if 'button_text4' not in st.session_state:
        st.session_state.button_text4 = "Click to record hotkey"

    if 'hotkey1' not in st.session_state:
        st.session_state.hotkey1 = 'placeholder'


    if 'listener' not in st.session_state:
        st.session_state.listener = "placeholder"


    if 'hotkey_value1' not in st.session_state:
        st.session_state.hotkey_value1 = 1

    if 'hotkey_value2' not in st.session_state:
        st.session_state.hotkey_value2 = 2

    if 'hotkey_value3' not in st.session_state:
        st.session_state.hotkey_value3 = 3


    if 'project_value1' not in st.session_state:
        st.session_state.project_value1 = "Default"

    if 'project_value2' not in st.session_state:
        st.session_state.project_value2 = "Default"

    if 'project_value3' not in st.session_state:
        st.session_state.project_value3 = "Default"


    col1, col2, _ = st.columns([1,1,1])

    project_list = []
    project_ids = []


    for element in st.session_state.enddata:
        project_list.append(element['name'])

    for element in st.session_state.enddata:
        project_ids.append(element['id'])

    id_to_name = {id: name for id, name in zip(project_list, project_ids)}


    def change_state():

        if st.session_state['button'] and not st.session_state.check:


            st.session_state.button_text = "Hotkeys activated. Click to deactivate."
            st.session_state.check = True


            # make sure to only activate hotkeys if they have been set
            hotkeylist = []

            if st.session_state.hotkey_value1 != 1:
                print('1')
                hotkeylist.append((st.session_state.hotkey_value1, st.session_state.project_value1))
            if st.session_state.hotkey_value2 != 2:
                print('2')
                hotkeylist.append((st.session_state.hotkey_value2, st.session_state.project_value2))
            if st.session_state.hotkey_value3 != 3:
                print('3')
                hotkeylist.append((st.session_state.hotkey_value3, st.session_state.project_value3))

            listener = hotkeys_finalversion.execute_hotkeys(hotkeylist)
            st.session_state.listener = listener


        elif st.session_state['button'] and st.session_state.check:
            st.session_state.button_text = "Hotkeys deactivated. Click to activate."
            st.session_state.check = False

            st.session_state.listener.stop()


    def record_hotkey1():

        a = scratch.main()

        st.session_state.button_text2 = a

        fset = frozenset(scratch.COMBINATIONS[0])
        print(fset)

        st.session_state.hotkey_value1 = fset

        scratch.COMBINATIONS.clear()

    def record_hotkey2():

        a = scratch.main()

        st.session_state.button_text3 = a

        fset = frozenset(scratch.COMBINATIONS[0])
        print(fset)

        st.session_state.hotkey_value2 = fset

        scratch.COMBINATIONS.clear()

    def record_hotkey3():

        a = scratch.main()

        st.session_state.button_text4 = a

        fset = frozenset(scratch.COMBINATIONS[0])
        print(fset)

        st.session_state.hotkey_value3 = fset

        scratch.COMBINATIONS.clear()




    with col1:

        st.write("Hotkey 1")
        second_button = st.button(st.session_state.button_text2, on_click=record_hotkey1, key='button_2',disabled=st.session_state.check)

        st.write("Hotkey 2")
        second_button = st.button(st.session_state.button_text3, on_click=record_hotkey2, key='button_3',
                                  disabled=st.session_state.check)
        st.write("Hotkey 3")
        second_button = st.button(st.session_state.button_text4, on_click=record_hotkey3, key='button_4',
                                  disabled=st.session_state.check)


    with col2:

        st.write("Select your project")

        option = st.selectbox("Select your project", (project_list), label_visibility="collapsed", index=1, key='selectbox1', disabled=st.session_state.check)

        selected_id = id_to_name[option]
        st.session_state.project_value1 = selected_id


        st.write("Select your project")
        option2 = st.selectbox("Select your project", (project_list), label_visibility="collapsed", index=2, key='selectbox2', disabled=st.session_state.check)



        selected_id2 = id_to_name[option2]
        st.session_state.project_value2 = selected_id2

        st.write("Select your project")
        option3 = st.selectbox("Select your project", (project_list), label_visibility="collapsed", index=3,
                               key='selectbox3', disabled=st.session_state.check)



        selected_id3 = id_to_name[option3]
        st.session_state.project_value3 = selected_id3

    # edge case 1: non-unique hotkeys chosen
    if st.session_state.hotkey_value1 == st.session_state.hotkey_value2 or st.session_state.hotkey_value2 == st.session_state.hotkey_value3 or st.session_state.hotkey_value3 == st.session_state.hotkey_value1:
        st.write('')
        st.error('You must choose unique hotkeys.', icon="🚨")
        st.session_state.start_check = True

    # edge case 2: non-unique projects chosen
    elif option == option2 or option2 == option3 or option == option3:
        st.write('')
        st.error('You must choose unique projects.', icon="🚨")
        st.session_state.start_check = True

    # edge case 3: no hotkey has been recorded yet
    elif st.session_state.button_text2 == st.session_state.button_text3 == st.session_state.button_text4:
        st.session_state.start_check = True
    else:
        st.session_state.start_check = False




    st.write('')
    first_button = st.button(st.session_state.button_text, on_click=change_state, key='button', disabled=st.session_state.start_check)

#2. if successfully authentificated: start main program
if st.session_state.enddata is not None:
    main(config.enddata)
