# comparision operator
a = input("Enter the number 1 :")
b = input("Enter the number 2 :")

if a>b:
    print("A is greater")
elif b>a:
    print("B is greater")
elif a==b:
    print("Equals")

# logical operator
# and or not
a = 10
if type(a) is int and a==10:
    print("A is integer and value is 10")
    
# Bitwise operator
# & |
a=3
b=2
print(a&b)
print(a|b)

# in operator
list1 = ['a','b','c','s','e']
a = 'b'
if a in list1:
    print("a value present in list")
else:
    print("not present in list")