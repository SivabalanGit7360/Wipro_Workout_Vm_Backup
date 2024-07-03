class Point:
    
    def __init__(self,xval,yval): # this special method called parameterized constructor
        self.x = xval
        self.y = yval  
        
    def showValues(self):
        print(f"x-val:{self.x},y-val:(self.y)")
        
    def anotherMethod(self):
        print(f"from another method: x-val:{self.x},y-val:{self.y}")
        
if __name__ == '__main__': # When imported value of __name__ will be equal to example
    p1 = Point(10,15)
    p1.anotherMethod()
    p1.showValues()