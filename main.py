import requests
from base64 import b64encode
import json
from datetime import datetime
import time
import keyboard
from threading import Thread

timeentry_id = 0
CS50 = 157781596
Mathematics = 165785237
Real_Analysis = 186010611

data = requests.get('https://api.track.toggl.com/api/v9/me/projects', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})
print(data.json())

def start_tracking(project_id):
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
    global timeentry_id
    timeentry_id = b['id']

def end_tracking():
    data = requests.patch(f'https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries/{timeentry_id}/stop',
        headers={'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(
        b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})

def started(project_id,hotkey):
    start_tracking(project_id)
    keyboard.remove_hotkey(hotkey)
    keyboard.add_hotkey(hotkey, ended, args=([project_id,hotkey]))

def ended(project_id,hotkey):
    end_tracking()
    keyboard.remove_hotkey(hotkey)
    keyboard.add_hotkey(hotkey, started, args=([project_id,hotkey]))

#Hotkeys

t1 = Thread(target=keyboard.add_hotkey("F1", started, args=([Mathematics,"F1"])))
t2 = Thread(target=keyboard.add_hotkey("F2", started, args=([CS50,"F2"])))
t3 = Thread(target=keyboard.add_hotkey("F3", started, args=([Real_Analysis,"F3"])))

