# perfect number

def is_Perfect(number):
    num_str = str(number)
    
    for digit in num_str:
        
        if digit == '0':
            return False
        if number % int(digit) != 0:
            return False
        return True
    
for num in range(141,152):
    result = is_Perfect(num)
    print(f"{num} is {'perfect' if result else 'not perfect'} ")
            