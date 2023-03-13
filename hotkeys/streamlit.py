import streamlit as st
from pynput import keyboard as pynputkeys
from scratches.main import enddata
from scratches.main_test import start_tracking, end_tracking
from scratches import config

if 'check' not in st.session_state:
    st.session_state.check = False

if 'listener' not in st.session_state:
    st.session_state.listener = False

if 'listener_start' not in st.session_state:
    st.session_state.listener_start = False


if 'hotkey_value1' not in st.session_state:
    st.session_state.hotkey_value1 = "Click to record hotkey"

if 'hotkey_value2' not in st.session_state:
    st.session_state.hotkey_value2 = "Click to record hotkey"

if 'hotkey_value3' not in st.session_state:
    st.session_state.hotkey_value3 = "Click to record hotkey"


if 'hotkey_code1' not in st.session_state:
    st.session_state.hotkey_code1 = '<112>'

if 'hotkey_code2' not in st.session_state:
    st.session_state.hotkey_code2 = '<113>'

if 'hotkey_codee3' not in st.session_state:
    st.session_state.hotkey_code3 = '<114>'

# write a check to block simultaneous hotkeys

if 'project_value1' not in st.session_state:
    st.session_state.project_value1 = "Default"

if 'project_value2' not in st.session_state:
    st.session_state.project_value2 = "Default"

if 'project_value3' not in st.session_state:
    st.session_state.project_value3 = "Default"


hotkey_list = []
hotkey_list.extend([st.session_state.hotkey_value1, st.session_state.hotkey_value2, st.session_state.hotkey_value3])

selected_projects = []
selected_projects.extend([st.session_state.project_value1, st.session_state.project_value2, st.session_state.project_value3])

if 'event_check' not in st.session_state:
    st.session_state.event_check = False

col1, col2, _ = st.columns([1,1,1])
project_list = []
project_ids = []

for element in enddata:
    project_list.append(element['name'])

for element in enddata:
    project_ids.append(element['id'])

id_to_name = {id: name for id, name in zip(project_list, project_ids)}

print(id_to_name)


def listener():
    with pynputkeys.Events() as events:
        # Block at most one second
        event = events.get()
        print(event)
        if event is None:
            print('You did not press a key within one second')
        else:
            print('Received event {}'.format(event))
        try:
            variable = event.key.value
        except AttributeError:
            variable = '<' + str(event.key.vk) + '>'

        try:
            naming = event.key.name
        except AttributeError:
            naming = event.key.char
        list22 = []
        list22.append(naming)
        list22.append(variable)
        return list22

# container = st.container()
# button_A = container.button(st.session_state.hotkey_value1, key=1)
#
# container2 = st.empty()
# button_B = container2.button(st.session_state.hotkey_value2, key=2)
#
# container3 = st.empty()
# button_C = container3.button(st.session_state.hotkey_value3, key=3)

with col1:

    st.write("Hotkey 1")
    placeholder = st.empty()
    button_A = placeholder.button(st.session_state.hotkey_value1, key=1)

    st.write("Hotkey 2")
    placeholder2 = st.empty()
    button_B = placeholder2.button(st.session_state.hotkey_value2, key=2)

    st.write("Hotkey 3")
    placeholder3 = st.empty()
    button_C = placeholder3.button(st.session_state.hotkey_value3, key=3)


    if button_A:
        value = listener()
        button_A = placeholder.button(value[0])
        st.session_state.hotkey_code1 = value[1]
        st.session_state.hotkey_value1 = value[0]

    if button_B:
        value = listener()
        button_B = placeholder2.button(value[0])
        st.session_state.hotkey_code2 = value[1]
        st.session_state.hotkey_value2 = value[0]

    if button_C:
        value = listener()
        button_C = placeholder3.button(value[0])
        st.session_state.hotkey_code2 = value[1]
        st.session_state.hotkey_value3 = value[0]

with col2:
    st.write("Select your project")
    option = st.selectbox("Select your project", (project_list), label_visibility="collapsed", index=1, key=4)
    selected_id1 = id_to_name[option]
    st.session_state.project_value1 = selected_id1
    st.write("Select your project")
    option2 = st.selectbox("Select your project", (project_list), label_visibility="collapsed", index=2, key=5)
    selected_id2 = id_to_name[option2]
    st.session_state.project_value2 = selected_id2
    st.write("Select your project")
    option3 = st.selectbox("Select your project", (project_list), label_visibility="collapsed", key=6)
    selected_id3 = id_to_name[option3]
    st.session_state.project_value3 = selected_id3

print(st.session_state.hotkey_value1)
print(st.session_state.hotkey_value2)
print(st.session_state.hotkey_value3)
print(st.session_state.hotkey_code1)
print(st.session_state.hotkey_code2)
print(st.session_state.hotkey_code3)
print(st.session_state.project_value1)
print(st.session_state.project_value2)
print(st.session_state.project_value3)



st.write("")
st.write("")
st.write("")

activate = st.empty()
st.session_state.hotkey_button1 = activate.button("Activate hotkeys", key=7)

global stop
stop = False

def on_activate_1():
    print("test")
    global stop
    if stop:
        end_tracking(config.time_entry)
        print("deactivated")
        stop = False
    elif not stop:
        start_tracking(157781596)
        stop = True
        print("activated")

def on_activate_2():
    print("test")
    global stop
    if stop:
        end_tracking(config.time_entry)
        print("deactivated")
        stop = False
    elif not stop:
        start_tracking(st.session_state.project_value2)
        stop = True
        print("activated")

def on_activate_3():
    print("test")
    global stop
    if stop:
        end_tracking(config.time_entry)
        print("deactivated")
        stop = False
    elif not stop:
        start_tracking(st.session_state.project_value3)
        stop = True
        print("activated")

print(st.session_state.check)

if st.session_state.hotkey_button1 and not st.session_state.check:
    if len(set(hotkey_list)) != len(hotkey_list):
        print("Duplicate keys detected")
        st.error("Duplicate hotkeys selected. Please choose a unique value for each hotkey.")
    if len(set(selected_projects)) != len(selected_projects):
        print("Duplicate keys detected")
        st.error("Duplicate projects selected. Please choose a unique project for each hotkey.")
    else:
        st.session_state.listener = pynputkeys.GlobalHotKeys({
            'b': on_activate_1,
            str(st.session_state.hotkey_code2): on_activate_2,
            str(st.session_state.hotkey_code3): on_activate_3})
        st.session_state.listener.start()
        st.session_state.check = True
        st.session_state.hotkey_button1 = activate.button("Deactivate hotkeys")

if st.session_state.hotkey_button1 and st.session_state.check:
    print(st.session_state.check)
    st.session_state.listener.stop()
    st.session_state.hotkey_button1 = activate.button("Activate hotkeys")
    st.session_state.check = False



