# Print all of the even numbers in the following list of nested lists. 
# This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

counter = 0
while counter < len(my_list):
    sub_counter = 0
    sub_list_length = len(my_list[counter])
    while sub_counter < sub_list_length:
        if my_list[counter][sub_counter] % 2 == 0:
            print(my_list[counter][sub_counter])
        sub_counter += 1
        
    counter += 1