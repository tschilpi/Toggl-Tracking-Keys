from base64 import b64encode
from datetime import datetime
import time
import requests
import json
import keyboard
from threading import Thread
import chime
import sys, os
#import win32gui
#import win32.lib.win32con as win32con
from pynput import keyboard as pynputkeys
import config
import streamlit as st

#Get user data
def fetch_user_data():
        data = requests.get('https://api.track.toggl.com/api/v9/me/projects', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(config.byte_string).decode("ascii")})
        try:
            config.enddata = data.json()
        except ValueError:
            st.error('Wrong API key entered.', icon="🚨")

#Function to start tracking
#Input for toggl's API (time_entries endpoint): check out official API's documentation to refers to how to set values (start, duration, etc.)
def start_tracking(project_id, bytestring):
    now = datetime.utcnow()
    # RFC 3339 required (add Z)
    utctime = now.isoformat() + "Z"
    # negative UNIX timestamp
    unixtime = int(-time.time())
    data = requests.post('https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries',
                         json={"created_with": "python", "pid": project_id, "workspace_id": 4005441,
                               "start": utctime, "user_id": 5446534, "duration": unixtime},
                         headers={'content-type': 'application/json',
                                  'Authorization': 'Basic %s' % b64encode(bytestring).decode("ascii")})
    b = json.loads(data.content)
    timeentry_id = b['id']
    chime.success()
    config.time_entry = timeentry_id


#Function to end tracking
#Refer to readme.txt to learn more about the event loop and how hotkeys are triggered
def end_tracking(timeentry_id, bytestring):
    data = requests.patch(f'https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries/{timeentry_id}/stop',
        headers={'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(
        bytestring).decode("ascii")})

    chime.success()






