# python  decorators

# decorators let you add extra behavior to a function
# without changing the function code

# a decorator is a function that takes another function as input and returns  a new function

# basic decorator

# define decorator first, then apply it with @decorator_name above the function
# a basic decorator that uppercases return value of the decorated function

def changeCase(func):
    def myinner():
        return func().upper()
    return myinner
@changeCase
def my_function():
    return "Hello Sally"

print(my_function())

# by placing @changeCase directly above the function definition, the function
# my function is being "decorated" with the changeCase function

# the function changeCase is the decorator that gets decorated

# multiple decorator calls
# a decorator can be called multiple times
# just place the decorator above the function you want to decorate

# using the @changeCase decorator on two functions:






# using the @changeCase decorator on two functions:

def changeCase(func):
    def myinner():
        return func().upper()
    return myinner

@changeCase
def my_function():
    return "Hello Sally"

@changeCase
def otherfunction():
    return "I am speed"

print(my_function())
print(otherfunction())

# arguments in the decorated function
# functions that requires arguments can also be decorated,
# just make sure you pass the arguments to the wrapper function:


# function with arguments can also be decorated

def changeCase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changeCase
def my_function(name):
    return "Hello " + name
print(my_function("John"))

# *args and **Kwargs
# sometimes the decorator function has no control over the arguments
# passed from decorated function, to solve this problem, add (*args, **kwargs)
# to the wrapper function, this way the wrapper function can accept any number,
# and any type of