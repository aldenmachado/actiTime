# Returning the function without
# executing it

# Closures is an inner function
# that remembers and has access to
# variables in the local scope in
# which it was created
# even after the outer function has finished exiting


def outer_func():

    ''' this is outer_func'''
    message = "Hi"

    # message is a free variable
    # inner function does not take any parameter
    # the inner function access the variable
    # which is called as free variable
    def inner_func():
        print(message)

    return inner_func

# When we execute the outer function
# it returns the inner function
# instead of executing it
# my _func variable is a function now
# which is equal to inner_func


my_func = outer_func()

# my_func is assigned to inner func
# prints inner_func
print(my_func.__name__)
print(my_func.__doc__)

# if my_func is executed
# it will print out the message
# as it is a function
# which returns the inner function
# but outer_func is executed

my_func()
my_func()
my_func()


