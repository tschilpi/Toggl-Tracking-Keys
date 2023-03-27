from datetime import datetime
import time
import requests
import json
import chime
import config
#import win32gui
#import win32.lib.win32con as win32con


#Get user data
def fetch_user_data():
        headers = {'content-type': 'application/json', 'Authorization': f'Basic {config.api_usage}'}
        data = requests.get('https://api.track.toggl.com/api/v9/me/projects', headers=headers)
        print(data.status_code)
        if data.status_code != 200:
            return None
        else:
            api_data = data.json()
            config.workspace_id = api_data[0]['workspace_id']
            return(api_data)

#Function to start tracking
#Input for toggl's API (time_entries endpoint): check out official API's documentation to refers to how to set values (start, duration, etc.)
def start_tracking(project_id):
    now = datetime.utcnow()
    # RFC 3339 required (add Z)
    utctime = now.isoformat() + "Z"
    # negative UNIX timestamp
    unixtime = int(-time.time())
    print(config.workspace_id)
    data = requests.post(f'https://api.track.toggl.com/api/v9/workspaces/{config.workspace_id}/time_entries',
                         json={"created_with": "python", "pid": project_id, "workspace_id": config.workspace_id,
                               "start": utctime, "duration": unixtime},
                         headers = {'content-type': 'application/json', 'Authorization': f'Basic {config.api_usage}'})
    b = json.loads(data.content)
    timeentry_id = b['id']
    chime.success()
    config.time_entry = timeentry_id


#Function to end tracking
#Refer to readme.txt to learn more about the event loop and how hotkeys are triggered
def end_tracking(timeentry_id):
    data = requests.patch(f'https://api.track.toggl.com/api/v9/workspaces/{config.workspace_id}/time_entries/{timeentry_id}/stop',
    headers={'content-type': 'application/json', 'Authorization': f'Basic {config.api_usage}'})

    chime.success()






