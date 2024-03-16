'''
Assume that obj already has a value of 42 when the code below starts running. 
Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? 
Which statements do neither? 
If necessary, you can read the documentation.
'''

obj = 'ABcd'            # reassign
obj.upper()             # neither
obj = obj.lower()       # reassign
print(len(obj))         # neither
obj = list(obj)         # reassign
obj.pop()               # mutates
obj[2] = 'X'            # mutates
obj.sort()              # mutates
set(obj)                # neither
obj = tuple(obj)        # reassign