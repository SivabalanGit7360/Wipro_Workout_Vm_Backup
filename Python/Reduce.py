# reduce - takes a sequence as arugument and returns a single values
# reduce can be imported from funtools

from functools import reduce

numbers = [x for x in range(1,20)]

# find the sum of numbers from 1 ... 19
# 1+2
# 3+3
# 6+4
# 10+5
# 15+6

total = reduce(lambda x,y: x+y, numbers)

print(total)