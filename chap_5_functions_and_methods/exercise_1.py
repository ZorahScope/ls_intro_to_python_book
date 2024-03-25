# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo) # 'foo' is not defined 

# because scope doesn't make it accessible outside the function it was initialized in. 
