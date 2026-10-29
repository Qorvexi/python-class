# PYTHON TUPLE

# Tuple is like a list, but you cannot change it once created.

colours = ("red", "green", "blue")

# Single item turple - you must add a comma, without a comma, python thinks it's a string
one_item = ("apple",)

# accessing tuple list values
print(colours[0])
print(colours[2])

# you cannot change a tuple
# no append(), remove(), no item assignment

# tuple length
len(colours)

# looping through a tuple
for colour in colours:
    print(colour)

# why use tuple?
# 1. when you want to protect data
# 2. you know the values should never change
# 3. for fixed data like:
days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

# tuple methods
numbers = (1, 2, 3, 2, 4, 3, 2, 8, 6, 2)
numbers.count(2) # how many 2s
numbers.index(3) # position of 3

# converting between list & tuple
# tuple to list (to modify)
x = ("joy", "ada", "tola")
y = list(x)


y.append("kemi")

# convert back to yuple using - tuple()
x = tuple(y)

# list to tuple
z = ["apple", "banana"]
z = tuple(z)

# assignment
# 1. define a list in python
# 2. define a tuple in python
# 3. state three differences between a list and a tuple
# 4. which of the data type ios mutable: list or tuple? explain what mutable means
# 5. give three life examples where a tuple is more suitable than a list
# 6. state whether the code is correct or wrong. if wrong, say why
# a. nums = (1, 2, 3)
#   nums.append(4)
# b. one = ("apple")
# c. names = ["Taiwo", "Bose"]
#   names[0] = "Bisi"

# 1.
# A list is an ordered, changeable (mutable) collection of items.

# 2.
# A tuple is an ordered, unchangeable (immutable) collection of items.

# 3. 
# Mutability 
# Syntax
# Performance

# 4.
# Lists are mutable.
# What does "mutable" mean?
# Mutable means that the object can be changed or modified after it has been created.

# 5. 
# GPS Coordinates (Latitude, Longitude)
# RGB Color Codes
# Database Records / User Credentials

# 6.
nums = (1, 2, 3)
nums.append(4)
# WRONG - nums is a tuple, and tuples are immutable. Tuples do not have an .append() method because you cannot add new elements to them after creation.

one = ("apple")
# WRONG
# Python does not treat ("apple") as a tuple; it treats it as a standard string "apple" wrapped in redundant parentheses. To define a single-item tuple, you must include a trailing comma: one = ("apple",).

names = ["Taiwo", "Bose"]
names[0] = "Bisi"
# CORRECT - names is a list (defined with []), and lists are mutable. Item replacement via index (names[0] = "Bisi") is fully supported. The list will now be ["Bisi", "Bose"]x♥♥