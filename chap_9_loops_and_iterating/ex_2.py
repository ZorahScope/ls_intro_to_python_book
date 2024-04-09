# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. 
# The updated code should use a for loop to display the future ages.

# submitted_age = int(input("How old are you?  "))
submitted_age = 30

print(f'You are {submitted_age} years old.')

for years in range(10,50,10):
    print(f'In {years} years, you will be {submitted_age + years} years old.')