# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718) 

# prints the 3 arguments provided when invoking the function, default values are ignored since a second & third argument was provided