# Dictionary . usiing {} curly brackets
# Consists of key value pairs
# key should be unique  and it should be immutable object

d1 = {
    
    "name" : "Siva",
    "age" : 24,
    "class" : "first"
    
}

print(d1)

print(d1['age'])

for k in d1:
    print(k)
    
for k,v in d1.items():
    print(k,v)
    
for k in d1.keys():
    print(k,d1[k])
    
print("\n#################")
list1 = ['name','age','class']
list2 = ['alice',7,'first']

list3 = list(zip(list1,list2))

print(list3)