# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# Raises an error, default value provided for 2nd parameter but not the 3rd.  