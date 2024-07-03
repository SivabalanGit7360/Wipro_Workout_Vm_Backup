# a number is termed as perfect provided all digits os the number are factor of the number

num = int(input("Enter the number :"))
t = num
while num:
    r = num%10
    if r==0 or t%r!=0:
        print("Not Perfect")
        break
        #num //= 10
    else:
        print("Perfect")
    