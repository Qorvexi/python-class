# python string formatting
# from lists import fruits
# from exercise import quantity

# f-strings
# f-string allows you to format selected parts of a string
# to specify a string as an f-string, simply put an f in front of the string
# literal, like this:


# create an f-string:
txt = f"The price is 49 dollars"
print(txt)

# placeholders and modifiers
# to format values in an f-string, add placeholders, {}, a placeholder can contain
# variables, operators, functions and modifiers to format the value

# add a placeholder for the place variable:
price = 59
txt = f"the price is {price} dollars"
print(txt)


# a placeholder can also include a modifier to format the value
# a modifier is included by adding a colon : followed by a legal formatting type
# like .2f which means fixed point number with 2 decimals:

# display the price with 2 decimals:
price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)







# perform operationsin f-strings
# you can perform python operations in the placeholder
# 
# you can do math operations


# perform a math operation in the placeholder, and return the result

txt = f"the price is {20 * 59} dollars"
print(txt)

# you can perform math operations on variables
# add taxes before displaying the price:

price = 59
tax = 0.25
txt = f"the price is {price + (price * tax)} dollars"
print(txt)


# you can perform if... else statements inside the placeholders:

# return "expensive" if the price is over 50, otherwise return "cheap":

price = 49
txt = f"the price is {"expensive" if price>50 else 'cheap'} dollars"
print(txt)


# execute functions in f-strings
# you can execute functions inside a placeholder:

# use the string method upper() to convert a value into upper case letters:

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# the function does not have to be a built-in python method, you can create your own
# create a function that converts feet into metres:

def myconverter(x):
    return x * 0.3048

txt = f"the plane is flying at a {myconverter(3000)} motor altitude"
print(txt)

# more modifiers
# at the beginning of this chapter we explained how to use the .2f modifier to format a number
# into a fixed point number with 2 decimals

# there are several other modifiers that can be used to format values:

# use a comma as a thousand separator:

# price = 59000
txt = f"the price is {price:,} dollars"
print(txt)

# string formt()

# the format method can still be used, but f-string