map = {'}':'(','}':'{',']':'['}

def fun(s1):
    for char in s1:
        if char in map.values():
            return "perfect"
        else:
            return "not"
        
s1 = "{{[]}(){}}"
#s1 = "sdfvfge456fdf"
print(fun(s1))