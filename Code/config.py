import os
from base64 import b64encode
global time_entry
global tracking1
tracking1 = False
global enddata
enddata = None


codename = os.getenv("FENDSYS_X23")
encoded_api_key = bytes(codename + ':api_token', encoding='ascii')
api_usage = b64encode(encoded_api_key).decode("ascii")

