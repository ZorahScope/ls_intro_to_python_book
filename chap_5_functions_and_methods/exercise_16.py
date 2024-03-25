def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# In the code shown below(above), identify all of the function names and parameters present in the code.  
# Include the line numbers for each item identified.

'''
multiply (func)         - Lines 1, 9
    left  (param)       - Lines 1, 2
    right (param)       - Lines 1, 2

get_num (func)          - Lines 4, 7, 8
    prompt (param)      - Lines 4, 5

float (func)            - Lines 5
input (func)            - Lines 5

print (func)            - Lines 10

'''
