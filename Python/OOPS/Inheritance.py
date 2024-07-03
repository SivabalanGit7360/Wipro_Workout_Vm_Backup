# Inherit class
class A:
    def printString(self):
        print("from A")
        
class B(A):
    pass

obj = B()
obj.printString() # calls parent class method

# multiple inheritance
class A:
    def printString(self):
        print("from A")
        
class B(A):
    def displayString(self):
        print("from child method")

obj = B()
obj.printString()
obj.displayString()

# multilevel inheritance

class E:
    def printString(self):
        print("from E")

class A:
    def printString(self):
        print("from A")
        
class C(E):
    pass
class B(C,A):
    pass
obj = B()
obj.printString()
print(B.__mro__) # return the order of execution

# mro - class attribute which the order execution when method is called

# MRO - method resolution order