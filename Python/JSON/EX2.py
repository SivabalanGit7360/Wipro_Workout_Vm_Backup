# get the python object from json file

import json

with(open("JSON/d2.json","r")) as fh:
    d3 = json.load(fh)
    print(d3)