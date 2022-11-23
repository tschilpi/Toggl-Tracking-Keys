import requests
from base64 import b64encode
import json
from datetime import datetime
import time

now = datetime.utcnow()
utctime = now.isoformat() + "Z"
unixtime = int(-time.time())

data = requests.get('https://api.track.toggl.com/api/v9/me/time_entries', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})
a = json.loads(data.content)

data = requests.post('https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries', json={"created_with":"python","pid":157781596,"workspace_id":4005441, "start":utctime,"user_id":5446534, "duration":unixtime}, headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})
b = json.loads(data.content)
timeentry_id = b['id']

time.sleep(10)

data = requests.patch(f'https://api.track.toggl.com/api/v9/workspaces/4005441/time_entries/{timeentry_id}/stop', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"1310a3434a655a92cb5cd3d26f9b4704:api_token").decode("ascii")})
print(data.json())