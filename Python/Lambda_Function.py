# lambda is a keyword for creating anonymous functions

# lambda returns function reference

# syntax for lambda
# lambda p1,p2,p3,.... body of lambda

# defining a lambda function

ref1 = lambda x: x*x
print(ref1) # print hexadecimal value

print(ref1(8)) #output will be 64

x = lambda a: a+10
print(x(5))

def myfunc(n):
    return lambda a: a*n
mydoubler = myfunc(2)
print(mydoubler(11))