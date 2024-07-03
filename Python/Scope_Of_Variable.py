# Scope of variable
# default scope is global
# global variable, local variable

# variable created inside the function is local variable
# 'global' keyword creating or accessing global variable with in function

x = 20

def f():
    y = 10
    print("Y inside a function: ",y)
f()

print("X is global scope: ",x)
print("Y is local scope: ",y)