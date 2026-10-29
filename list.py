# PYTHON LIST

# A list is a container that can hold many values at once.
names = ["mide", "gbenga", "tiwa"]

# A list can store strings, numbers, booleans and even mixed data types!
mixed = ["joy", 20, True, 5.5]

# Empty list
empty_list = []

fruits = ["orange", "grape", "apple"]

# create a list of ten colours, store it in a variable
colours = ["sky blue", "white", "black", "gold", "royal blue", "yellow", "dark blue", "gray", "green", "orange"]

# ACCESSING ITEMS (INDEXING/POSITION)
# Indexing starts from 0
names = ["mide", "gbenga", "tiwa"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# CHANGING ITEMS
# Lists are mutables (you can modify them)
fruits[1] = "Mango"
print(fruits)

# ADDING TO A LIST
# 1. .append() - adds to the end
fruits.append("pineapple")
fruits.append("Watermelon")
print(fruits)

# 2. .insert() - adds to a position
fruits.insert(1, "cherry") 
print(fruits)
fruits.insert(4, "dragon fruit")
print(fruits)

# REMOVING ITEMS
fruits.remove("apple")
print(fruits)
fruits.pop() # removes last item
print(fruits)
fruits.pop(1) # removes item at index 1
print(fruits)

# LIST LENGTH  - using the len() function 
total_fruits = len(fruits)
print(total_fruits)

# LOOPING THROUGH A LIST
for fruit in fruits:
    print(fruit)

# EXTRA METHODS
fruits.sort() # sort alphabetically
fruits.reverse() # reverse order
fruits.clear() # remove anything

# CLASS EXERCISE
# CREATE A LIST OF 5 MOVIES YOU HAVE WATCHED SO FAR
# print:
# first movie
# last movie

# CREATE A LIST O9F 10 FOOTBALLERS
# change the second item to a different footballer
# sort their names alphabetically

# create an empty list to store nigerian dishes
# on the next line, add:
# eba, beans, semo, egusi and moi-moi.
# insert garri at index 3. insert fufu at index 2
# remove first item, remove the last item, remove an item at index 3

movies = ["the northman", "fast n furious", "IT", "the nun", "off campus"]
print(movies)
print(movies[0])
print(movies[4])

footballers = ["Neymar jnr", "Lionel Messi", "Erling Haaland", "Rayan Cherki", "Casemiro", "Rodri", "Nico O'Reilly", "Marquinhos", "Gabriel Magalhaes", "Matheus Nunes"]
print(footballers)
footballers[1] = "Raphinha"
print(footballers)
order = footballers.sort()
print(footballers)

dish = []
print(dish)
dish.append("Eba")
dish.append("Beans")
dish.append("Semo")
dish.append("Egusi")
dish.append("Moi-Moi")
print(dish)
dish.insert(2, "Fufu")
dish.insert(3, "Garri")
print(dish)
dish.pop(0)
dish.pop(5)
dish.pop(3)
print(dish)