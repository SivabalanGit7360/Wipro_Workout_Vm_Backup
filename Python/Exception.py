# Expection
  
try:
    print(x)
except:
    print("An Exception occurred")
    
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
    
# Using Else

try:
    print("Hello")
except :
    print("Something went wrong")
else:
    print("Nothing went wrong")
    
# Finally

try:
    print(x)
except:
    print("Something else went wrong")
finally:
    print("The 'try expect' is finished" )