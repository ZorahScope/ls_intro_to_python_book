# Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

def has_3(lst):
    if (3 in lst):
        print(True)
    else:
        print(False)

has_3(numbers1)
has_3(numbers2)
has_3(numbers3)
has_3(numbers4)
has_3(numbers5)