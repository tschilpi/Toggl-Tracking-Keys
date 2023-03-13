import streamlit as st
from pynput import keyboard as pynputkeys
import scratch
import main_test
import hotkeys_finalversion
import config


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


if 'listener1' not in st.session_state:
    st.session_state.listener1 = "placeholder"

if 'listener2' not in st.session_state:
    st.session_state.listener2 = "placeholder"

if 'listener3' not in st.session_state:
    st.session_state.listener3 = "placeholder"


if 'hotkey_value1' not in st.session_state:
    st.session_state.hotkey_value1 = None

if 'hotkey_value2' not in st.session_state:
    st.session_state.hotkey_value2 = None

if 'hotkey_value3' not in st.session_state:
    st.session_state.hotkey_value3 = None


if 'project_value1' not in st.session_state:
    st.session_state.project_value1 = "Default"

if 'project_value2' not in st.session_state:
    st.session_state.project_value2 = "Default"

if 'project_value3' not in st.session_state:
    st.session_state.project_value3 = "Default"


col1, col2, _ = st.columns([1,1,1])

project_list = []
project_ids = []

for element in main_test.enddata:
    project_list.append(element['name'])

for element in main_test.enddata:
    project_ids.append(element['id'])

id_to_name = {id: name for id, name in zip(project_list, project_ids)}


def change_state():

    if st.session_state['button'] and not st.session_state.check:


        st.session_state.button_text = "Hotkeys activated. Click to deactivate."
        st.session_state.check = True


        listener = hotkeys_finalversion.execute_hotkeys(st.session_state.hotkey_value1, st.session_state.project_value1)
        st.session_state.listener1 = listener


        listener2 = hotkeys_finalversion.execute_hotkeys(st.session_state.hotkey_value2,
                                                        st.session_state.project_value2)
        st.session_state.listener2 = listener2


        listener3 = hotkeys_finalversion.execute_hotkeys(st.session_state.hotkey_value3,
                                                             st.session_state.project_value3)
        st.session_state.listener3 = listener3


    elif st.session_state['button'] and st.session_state.check:
        st.session_state.button_text = "Hotkeys deactivated. Click to activate."
        st.session_state.check = False

        st.session_state.listener1.stop()
        st.session_state.listener2.stop()
        st.session_state.listener3.stop()


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

#edge cases: duplicate hotkeys or duplicate projects
if st.session_state.hotkey_value1 == st.session_state.hotkey_value2 or st.session_state.hotkey_value2 == st.session_state.hotkey_value3 or st.session_state.hotkey_value3 == st.session_state.hotkey_value1 or option == option2 or option2 == option3 or option == option3:
    st.write('')
    st.error('Please make sure to record unique hotkey values and select unique projects.', icon="🚨")
    st.session_state.start_check = True
else:
    st.session_state.start_check = False


st.write('')
first_button = st.button(st.session_state.button_text, on_click=change_state, key='button', disabled=st.session_state.start_check)


