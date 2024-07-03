numbers = [x for x in range(50)]

even_numbers = list(filter(lambda x: x%2==0, numbers))

print(even_numbers)