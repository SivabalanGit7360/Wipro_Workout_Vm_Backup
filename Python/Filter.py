numbers = [x for x in range(50)]
print(numbers)
def sort_fn(x):
    return x%2==0

# filter using custom function

even_numbers = list(filter(sort_fn,numbers))

print(even_numbers)