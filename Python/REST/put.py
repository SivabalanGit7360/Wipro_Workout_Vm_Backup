import requests
import json

r = requests.put("https://reqres.in/api/users/2",
                 json={"name":"Krishna","job":"Developer"})

if r.status_code == 200:
    d1 = json.loads(r.text)
    print(d1)
    
else:
    print("unable to access", r.status_code)