# Identify all of the identifiers on each line of the following code.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

'''
multiply        lines 1,11
left            lines 1 & 2
right           lines 1 & 2
get_num         lines 6, 9 & 10
prompt          lines 6 & 7
first_number    lines 9, 11, & 12
second_number   lines 10, 11, & 12
product         lines 11 & 12
float           line 7
input           line 7
print           line 12
'''