# tuple is immutable
# single tuple needs ,

tuple1 = (10,'hello',20,'world',40.35) # using parenthesis
tuple2 = 10,'hello',20,'world',40.35 # by asscessing ,

print(tuple1)

print("\n*************")

print(tuple2)

# tuple1[1]='h1' # it give error
# print(tuple1)

tuple1 = (10,20,30,40) # overwritten with new values
print(tuple1)

t1 = (10)
print(type(t1))

t2 = 10,20.30,45,10 # , is important
print(type(t2))



