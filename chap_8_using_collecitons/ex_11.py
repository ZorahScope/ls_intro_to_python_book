# Without running the following code, determine what each line should print.

print('johnson' in 'Joe Johnson')       # false, no lowercase johnson
print('sen' not in 'Joe Johnson')       # true
print('Joe J' in 'Joe Johnson')         # true
print(5 in range(5))                    # false, ending range not inclusive
print(5 in range(6))                    # true
print(5 not in range(5, 10))            # false, starts with 5
print(0 in range(10, 0, -1))            # false, ending range no inclusive
print(4 in {6, 5, 4, 3, 2, 1})          # true  
print({1, 2, 3} in {1, 2, 3})           # false
print({3, 2} in {1, frozenset({2, 3})}) # true