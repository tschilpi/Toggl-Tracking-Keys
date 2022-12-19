import requests
from base64 import b64encode
import json
from datetime import datetime
import time
import keyboard
from threading import Thread
import chime

#toggl time entry globally declared
#project id's of the hotkeys

CS50 = 157781596
Mathematics = 165785237
Real_Analysis = 186010611

#Get user data
data = requests.get('https://api.track.toggl.com/api/v9/me/projects', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})
print(data.json())

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

#Hotkey event started separately, in parallel, with threads

t1 = Thread(target=keyboard.add_hotkey("F1", start_tracking, args=([Mathematics,"F1"])))
t2 = Thread(target=keyboard.add_hotkey("F2", start_tracking, args=([CS50,"F2"])))
t3 = Thread(target=keyboard.add_hotkey("F3", start_tracking, args=([Real_Analysis,"F3"])))

