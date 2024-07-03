# Featuress of OOPS

# encapsulation - place all methods and variables inside a entity called class
# inheritance - Getting the properties of parent class inside child class
                 
# abstraction - hiding the implementation details
# polymorphism - multiple version of same method ( method overriding)

class Point: # class
    
    def showValues(self):
        print("This is an instance method")
        
if __name__ == '__main__':
    p1 = Point() # object creation for point class
        
   # print(p1.__doc__) # get the documentation string
        
    p1.showValues()
    
    
        