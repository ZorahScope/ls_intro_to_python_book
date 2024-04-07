# What will the following code print?

print('abc-def'.isalpha())      # false, since '-' is not a letter
print('abc_def'.isalpha())      # false, since '_' is not a letter
print('abc def'.isalpha())      # false, since '' is not a letter
print('abc def'.isalpha() and
      'abc def'.isspace())      # false, ' ' is not a letter
print('abc def'.isalpha() or
      'abc def'.isspace())      # false
print('abcdef'.isalpha())       # true
print('31415'.isdigit())        # true
print('-31415'.isdigit())       # false, '-' is not a digit
print('31_415'.isdigit())       # false, underscore not digit
print('3.1415'.isdigit())       # false '.' not digit
print(''.isspace())             # false, empty str doesn't have space