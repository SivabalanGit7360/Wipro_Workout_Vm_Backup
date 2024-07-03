# generate numbers upto 200. Use filter and lambda to select elements divide by 8
numbers = [x for x in range(200)]

divided_numbers = list(filter(lambda x: x%8==0, numbers))

print(divided_numbers)