# Arguments
# Imformation can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parenthesis.
# You can add as many arguments as you like, just separate it with a comma

# The following example has a function with one argument(fname)
# when the function is called, we pass along a first name, which is used inside
# the function to print the full name:


# A function with one argument:

def my_function(fname):
    print(fname + " Welcome")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# parameters vs arguments
# the terms parameter and argument can be used for the same thing:
# information that are passed into a function

# from a function's perspective

# a parameter is a variable listed inside a parentheses in the function definition

# an argument is the actual value that is sent to the function when it is called.


def my_function(name): # name is a parameter
    print("Hello", name)

my_function("Emil") # "Emil" is an argument


# Number of arguments
# by default, a function must be called with the correct number of arguments

# if your functionexpects two arguments, you must call it with exactly two arguments


# this function expects two arguments, and gets two arguments:

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# if you try to call the function with the wrong number of arguments,
# you will get an error:


# this function expects 2 arguments, but gets only one

def my_function(fname, lname):
    print(fname + " " + lname)

# my_function("Emil")

# default parameter value
# you can assign defayult values to pearmeters. if the function is
# called without an argument,
# it uses the default value:

def my_function(name = "friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# defaultvalue for country parameters:

def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Keyword arguments
# you can send arguments with the key = value syntax

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
my_function("dog", "Buddy")
my_function(name="Bobby", animal="dog")

def my_function(name, food):
    print(f"My name is {name}, my fav food is {food}")

def my_function(food = "Semo & vegies", name = "Larry"):
    # This way, with keyword arguments, the order of the arguments, the order of the arguments does not matter

    def my_function(animsl, name):
        print("I have a", animsl)
        print("My", animsl + "'s name is", name)

my_function(name = "Buddy", animal = "dog")


# the phrase keyword arguments is often shortened to kwargs n python documentation

# positional arguments
# when you call a function with arguments without using keywords,
# they are called positional arguments

# positional arguments mustn be in the correct order:
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# the order matters with positional arguments:
# switching the order changes the result:

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

# mixing positional and keyword arguments
# you can mix positional and keyword arguments in a function call

# however, positiional arguments must come bafore keyword arguments

def my_function(animal, name, age):
    print("I have a", age, "years old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# passing different data types
# you can send any data type as an argument to a function (string, number, list, dict)

# the data type will be preserved inside the function:

# sending a list as an argument:

def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# sending a dictionary as an argument:
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 23}
my_function(my_person)

# return values
# functions can return values using the return ststement

def my_function(x, y):
    return x + y

result = my_function(1, 2)
print(result)

# returning different data types
# functions can return any data type, including lists, tuples, dictionaries and more

# a function that returns a list:

def my_function():
    return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# a function that returns a tuple:

def my_function():
    return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

# positional-only arguments
# you can specify that a function can have only positional arguments

# to specify positional-only, add, / after the arguments:

def my_function(name, /):
    print("Hello", name)

my_function("Emil")

# without the, / you are actually allowed to use keyword arguments even if
# the function expects positional arguments

def my_function(name):
    print("Hello", name)

my_function(name = "Emil")

# with, /, you will get an error if you try to use keyword arguments

def my_function(name, /):
    print("Hello", name)

# my_function(name = "Emil")

# keyword-only arguments
# to specify that a function can have only keyword arguments:

def my_function(*, name):
    print("Hello", name)

my_function(name = "Emil")


# without *, you are allowed to use positional arguments even if the function expects keyword arguments:

def my_function(name):
    print("Hello", name)

my_function("Emil")

# with *, you will get an error if you try to use positional arguments


def my_function(*, name):
    print("Hello", name)

# my_function(name = "Emil")

# combining positional -only and keyword only, and arguments after * are keyword-only

def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)