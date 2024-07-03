num = int(input("Enter the number :"))

v = 0

for n in range(2,num):
    if n%num==0:
        v=1
        break
if v:
    print("Not prime")
else:
    print("Prime")
