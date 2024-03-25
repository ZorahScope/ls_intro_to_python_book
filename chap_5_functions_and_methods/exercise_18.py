# The following function returns a list of the remainders of dividing the numbers in numbers by 3: 

def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print("Number 1: " + str(remainders_3(numbers_1) ))
print("Number 2: " + str(remainders_3(numbers_2) ))
print("Number 3: " + str(remainders_3(numbers_3) ))
print("Number 4: " + str(remainders_3(numbers_4) ))

# Answer: lists 1 & 2