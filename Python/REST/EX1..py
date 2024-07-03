import requests
import json

data = {"name": "morpheus","job": "leader"} # this is dictionary
headers = {'Content-type': 'application/json'}

r = requests.post("https://reqres.in/api.users",headers=headers,data=json.dumps(data))

if r.status_code == 201:
    d1 = json.loads(r.text)
    print(d1)
    
else:
    print("unable to access", r.status_code)