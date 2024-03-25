# Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    print(f'{first} * {second} = {first * second}')

multiply()
