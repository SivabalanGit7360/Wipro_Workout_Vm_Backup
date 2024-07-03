for i in range (10):
    print(i)
    
    
for i in range (1,10):
    print(i)
  
# Immutable object
print("-----------------------")
a=5
print(a)
print(id(a))

print("-----------------------")

a += 2 # Modifying the object
print(a)
print(id(a))

# mutable object

print("-----------------------")

list1 = [10,20,30]
print(list1)
print(id(list1))

list1[1] = 100
print(list1)
print(id(list1))