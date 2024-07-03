def f(x):
    def g():
        return x*x
    return g

v = f(10) # returns the reference of g
print(v) # displays the reference of g
print(v()) # call the inner function g using its reference