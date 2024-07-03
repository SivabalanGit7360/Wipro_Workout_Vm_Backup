# consuiming restapi and get a dictionary from a json object

import requests
import json

r = requests.get("https://reqres.in/api/users?page=2")


if r.status_code == 200:
    print(type(r.text))
    d1 = json.loads(r.text)
    print(d1)
    
else:
    print("could not get result from rest and point")