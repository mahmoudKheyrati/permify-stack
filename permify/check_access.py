import requests


import json
import requests

url = "http://localhost:3476/v1/tenants/t1/permissions/check"
headers = {"Content-Type": "application/json"}

payload = {
  "metadata": {
    "schema_version": "civ7dopb0mjs73aupu10",
    "snap_token": "KyOVrI3PdBc=",
    "depth": 20
  },
  "entity": {
    "type": "organization",
    "id": "1"
  },
  "permission": "view_files",
  "subject": {
    "type": "user",
    "id": "1",
    "relation": ""
  }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Status = ",response.text)
else:
    print("Error", response.text)