# Method overriding - re implement parent class method in child class

class A:
    def printString(self):
        print("from A")
        
class B(A):
    def displayString(self):
        print("from child method")
        
    def printString(self): # re implementation of parent class method
        print("from B")

obj = B()
obj.displayString()
obj.printString()