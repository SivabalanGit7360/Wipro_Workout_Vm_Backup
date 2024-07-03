import json

d2 = {"name":"bob", "age":10, "class":"first"}

#fh = open("d1.json","w")

with(open("JSON/d2.json","w")) as fh:
    json.dump(d2,fh)

#fh.close()