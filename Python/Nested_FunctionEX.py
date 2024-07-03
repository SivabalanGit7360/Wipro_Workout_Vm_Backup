def f(x):
    def g(y):
        return y*y
    return x+g(x)

# calling nested function

retval = f(10)
print(retval)