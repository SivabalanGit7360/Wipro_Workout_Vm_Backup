# convert a python object to json string

import json

d1 = {"name":"bob","age":10,"class":"first"}

print(type(d1))

s1 = json.dumps(d1)

print(type(s1))

print(s1)