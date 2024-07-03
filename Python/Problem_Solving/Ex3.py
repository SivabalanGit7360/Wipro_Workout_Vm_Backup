# Highest sum of adjamcent number
list1 = {12,30,-15,24,68}
max = 0
for i in range(len(list1)-1):
    sum = list1[i]+list1[i+1]
    if max<sum:
        max=sum
    print(max)
        