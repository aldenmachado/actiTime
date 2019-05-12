# Decorators

# First class functions
# allows us to treat functions
# as any other object
# Closures allow us to take advantage of first
# class functions that remembers and has access
# to variables local to the scope in which
# they were created

# Decorator: A function which takes
# another function as an argument
# adds some kind of functionality
# and returns another function
# without altering the source code
# of the original passed in

# Example

# returns wrapper function
# waiting to be excited

# original function would be equal to
# the argument passed in the decorator
# function

# without modifying the original display
# function, we can modify the
# wrapper function which is waiting to be
# exeucted


def decorator_function(original_function) -> string:
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))

        # wrapper function is waiting
        # to be executed
        # wrapper function executes
        # the original function
        # that we have passed in

        return original_function()
    return wrapper_function

# Decorator executes a function

# Similar to setting
# the original function
# equal to the wrapped function
# display = decorator_function(display)
# original function is run with
# decorator applied


@decorator_function
def display():
    print('display function ran')

# Function is passed
# as variable argument
# inside another function
# which would be then
# called by the wrapper function
# without modifying the code of the original function


display()



