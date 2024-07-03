text = "Goos to see"

# string to uppercase using upper() function
print("\nConverted String")
print(text.upper())

# string to lowercase using lower() function
print("\nConverted String")
print(text.lower())

# Convert the first character to uppercase and rest to lowercase using tittle() function
print("\nConverted String")
print(text.title())

list1 = ['siva@gmail.com','Tharun@gmail.com','Krishna@gmail.com']

for element in list1:
    if element.endswith('@gmail.com'):
        print("Present " + element)