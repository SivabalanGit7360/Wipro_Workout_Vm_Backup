
def my_function():
    print("Hello from a function")
    
my_function()

def findName(fname):
    print(fname + " I am Good")

findName("Krishna")
findName("Ragu")
findName("Siva")

def name(*TeamName):
    for i in range(len(TeamName)):
      print(TeamName[i])
      
name("Rohit","Khoil","Surya","Bumbrah")
