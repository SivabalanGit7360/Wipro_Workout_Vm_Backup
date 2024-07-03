class Point:
    
    def showValues(self):
        self.x = 25 # self.x and self.y are called instance attribute
        self.y = 30
        print(f"x-val:{self.x},y-val:(self.y)")
        
    def anotherMethod(self):
        print(f"from another method: x-val:{self.x},y-val:{self.y}")
        
if __name__ == '__main__': # Whwn imported value of __name__ will be equal to example
    p1 = Point()
    p1.anotherMethod()
    p1.showValues()