# create a constructor
class Point:
    
    def __init__(self): # this special method called constructor
        self.x = 25
        self.y = 30  # self.x and self.y are called instance attribute
        
    def showValues(self):
        print(f"x-val:{self.x},y-val:(self.y)")
        
    def anotherMethod(self):
        print(f"from another method: x-val:{self.x},y-val:{self.y}")
        
if __name__ == '__main__': # When imported value of __name__ will be equal to example
    p1 = Point()
    p1.anotherMethod()
    p1.showValues()