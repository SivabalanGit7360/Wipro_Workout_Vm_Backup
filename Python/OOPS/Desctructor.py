# destructor - is invoked when the object get destroyed
class Point:
    
    def __init__(self,xval,yval): # this special method called constructor
        self.x = xval
        self.y = yval  
        #Point.num_of_points += 1
        
    def showValues(self):
        print(f"x-val:{self.x},y-val:(self.y)")
        
    def anotherMethod(self):
        print(f"from another method: x-val:{self.x},y-val:{self.y}")
        
    def __del__(self): # this special method called destructor constructor
        print("desctructor called")
        
if __name__ == '__main__': # When imported value of __name__ will be equal to example
    p1 = Point(10,15)
    p2 = Point(13,17)
   # p1.anotherMethod()
   # p1.showValues()
    
    del p1,p2