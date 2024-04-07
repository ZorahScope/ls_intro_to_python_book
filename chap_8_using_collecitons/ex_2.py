# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

ls = 'Launch School'
idx = ls.find('c')
print(ls[idx:idx+6])