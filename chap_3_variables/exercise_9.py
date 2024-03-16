'''
Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.
'''

balance = 1_000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05

print(f'{balance:.2f}')
