import os
from base64 import b64encode
time_entry = None
tracking1 = False
enddata = None
workspace_id = None
env_variable = None
api_usage = None

def update_env_variable(value):
    global env_variable, api_usage
    env_variable = value

    codename = os.getenv(env_variable)
    encoded_api_key = bytes(str(codename) + ':api_token', encoding='ascii')
    api_usage = b64encode(encoded_api_key).decode("ascii")
