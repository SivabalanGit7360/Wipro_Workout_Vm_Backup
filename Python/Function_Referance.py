def square(x):
    return x*x

print(square(8)) # output will be 64

print(square) # function referance in hexadecimal form

ref1 = square # assign the function referance to a variable

print(ref1)# function referance in hexadecimal form

print(ref1(10))

def f(x):
    return x**2

print(f(10))