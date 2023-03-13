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

#toggl time entry globally declared
#project id's of the hotkeys

CS50 = 157781596
Mathematics = 165785237
Real_Analysis = 186010611

global dead
dead = False

#Get user data
data = requests.get('https://api.track.toggl.com/api/v9/me/projects', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})
print(data.json())
enddata = data.json()

#Function to start tracking
#Input for toggl's API (time_entries endpoint): check out official API's documentation to refers to how to set values (start, duration, etc.)
def start_tracking(project_id, hotkey):
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
                                      b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})
    b = json.loads(data.content)
    timeentry_id = b['id']

    chime.success()
    keyboard.remove_hotkey(hotkey)
    keyboard.add_hotkey(hotkey, end_tracking, args=([timeentry_id, project_id, hotkey]))

#Function to end tracking
#Refer to readme.txt to learn more about the event loop and how hotkeys are triggered
def end_tracking(timeentry_id, project_id, hotkey):
    data = requests.patch(f'https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries/{timeentry_id}/stop',
        headers={'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(
        b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})

    keyboard.remove_hotkey(hotkey)
    chime.success()
    keyboard.add_hotkey(hotkey, start_tracking, args=([project_id, hotkey]))

hotkey_thread = None
stop_flag = threading.Event()

#Hotkey event started separately, in parallel, with threads

def hotkey_tracking(hotkey1, hotkey2, hotkey3, project1_id, project2_id, project3_id):

    global hotkey_thread
    global stop_flag

    if hotkey_thread is None:
        hotkey_thread = threading.Thread(target=keyboard.add_hotkey(hotkey1, start_tracking, args=([project1_id,hotkey1])))

    else:
        stop_flag.set()
        hotkey_thread.join()
        hotkey_thread = None
        stop_flag.clear()

    # t2 = Thread(target=keyboard.add_hotkey(hotkey2, start_tracking, args=([project2_id,hotkey2])))
    # t3 = Thread(target=keyboard.add_hotkey(hotkey3, start_tracking, args=([project3_id,hotkey3])))

# the_program_to_hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

input()
