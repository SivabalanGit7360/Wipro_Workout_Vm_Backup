list1 = ["apple","banana","cherry","strawberry"]
print(list1)

print(len(list1))

list2 = list1
print("Reference of list1 : ",id(list2))
print("Reference of list1 : ",id(list1))

#Create a copy of list1

list3 = list1.copy()
list4 = list1[:] # this also copy
print("This is list 3 value :",list3)
print("This is list 4 value :",list4)

list1.remove('apple')
print(list1)

list1.append("Kiwi")
print(list1)

list1.insert("Mango")
print(list1)
list1.pop()