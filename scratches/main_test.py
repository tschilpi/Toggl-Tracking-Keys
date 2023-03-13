import requests
from base64 import b64encode
import json
from datetime import datetime
import time
import keyboard
from threading import Thread
import chime
import threading
import sys, os
import win32gui
import win32.lib.win32con as win32con
from pynput import keyboard as pynputkeys
import config
import streamlit as st

#toggl time entry globally declared
#project id's of the hotkeys

CS50 = 157781596
Mathematics = 165785237
Real_Analysis = 186010611

st.title('Global Hotkeys for Toggl :sunglasses:')
st.write('')
st.write('')

with st.form('test', clear_on_submit=True):
    input = st.text_input('Please input your API key.', key=10)
    st.form_submit_button()

st.write('')

config.API_KEY = input
API_TOKEN = config.API_KEY
byte_string = bytes(API_TOKEN + ':api_token', encoding='ascii')
print(byte_string)

#Get user data
data = requests.get('https://api.track.toggl.com/api/v9/me/projects', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(byte_string).decode("ascii")})
print(data.json())
enddata = data.json()

#Function to start tracking
#Input for toggl's API (time_entries endpoint): check out official API's documentation to refers to how to set values (start, duration, etc.)
def start_tracking(project_id):
    global time_entry
    now = datetime.utcnow()
    # RFC 3339 required (add Z)
    utctime = now.isoformat() + "Z"
    # negative UNIX timestamp
    unixtime = int(-time.time())
    data = requests.post('https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries',
                         json={"created_with": "python", "pid": project_id, "workspace_id": 4005441,
                               "start": utctime, "user_id": 5446534, "duration": unixtime},
                         headers={'content-type': 'application/json',
                                  'Authorization': 'Basic %s' % b64encode(
                                      byte_string).decode("ascii")})
    b = json.loads(data.content)
    timeentry_id = b['id']
    chime.success()
    config.time_entry = timeentry_id

#Function to end tracking
#Refer to readme.txt to learn more about the event loop and how hotkeys are triggered
def end_tracking(timeentry_id):
    data = requests.patch(f'https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries/{timeentry_id}/stop',
        headers={'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(
        byte_string).decode("ascii")})

    chime.success()





