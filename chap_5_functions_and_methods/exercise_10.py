# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

'''
=> 42
=> 3.141592
=> 2

prints the 2 arguments provided and uses the default value 2 since a "third" argument wasn't given

'''