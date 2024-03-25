foo = 'bar'

def set_foo():
    foo = 'qux'


set_foo()
print(foo)  # => 'bar'

# What does this program print? Why?

# the assignment inside the function on line 4 initializes foo as a local variable 
# this doesn't affect the globally scoped "foo" that gets printed on line 8 despite the invocation on line 7 assigning foo to 'qux'