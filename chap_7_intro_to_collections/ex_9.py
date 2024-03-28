my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

'''
Given the above code, answer the following questions and explain your answers:

    1. Are the lists assigned to my_list and another_list equal?                  Yes, they are both lists with matching elements

    2. Are the lists assigned to my_list and another_list the same object?        No, The list constructor creates a new list object

    3. Are the nested lists at index 3 of my_list and another_list equal?         Yes, they have the same elements

    4. Are the nested lists at index 3 of my_list and another_list the same object?     Yes,  the list constructor only creates a shallow copy which don't affect nested lists

'''