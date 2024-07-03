import requests
import json

r = requests.delete("https://reqres.in/api/users/2")

if r.status_code == 204:
    print("record deleted")
else:
    print("unable to access", r.status_code)