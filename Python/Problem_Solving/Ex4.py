# find max

def find_max(*args):
    
    print(type(args))
    m = args[0]
    
    for v in args:
        if m<v: m=v
    return m
max_Val = find_max(83,405,81,76,45)
print(max_Val)

max_Val = find_max(78,980,1245,700,850,905,999)
print(max_Val)

# kwargs inside the function treated as dictionary

def multipleParams(**kwargs):
    
    print(kwargs)
    
multipleParams(name="krishna", age = 24,company = "capgemini")