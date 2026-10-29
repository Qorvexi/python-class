# Dictionary
# dictiionaries are used to store data values in key value pairs
# dictionary is a collection which is ordered, changeable, and do not allow duplicates
# dictionaries are wwritten with curly braces, and have keys and values:

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1964",
}

print(thisdict)

# dictionary length
# to determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# dictionary data types
# the values in dictionary has items can be of any data type:


vehicle = {
    "brand": "toyota",
    "electric": False,
    "year": 1965,
    "colors": ["silver", "black", "wine"]
}

# using the dict() constructor method to make a dictionary:

thisdict = dict(name="john", age=36, country="brazil")
print(thisdict)

# Accessing items
# you can access the items of a dictuionary by referring to the key name,
# inside square brackets

car = {
    "brand": "lamborghini",
    "model": "revuelto",
    "year": 2025
}

x = car["model"]
print(x)

y = car["year"]
print(y)

z = car["brand"]
print(z)

# there is also a method called get() that will give you the same result:

y = car.get("model")
print(y)

# get keys
# rhe keys() method will return a list of all the keys in the dictionary.
x = car.keys()
print(x)

# add a new item to the original dictionary, and see that the keys list gets
# updated as well:

phone = {
    "brand": "apple",
    "model": "iphone 15 pro max",
    "year": "2024"
}

x = phone.keys()
print(x) # before the change

phone["color"] = "pink" # value to our dictionary
print(phone)
print(x) # after change

# gety values
# the values method will return all the values in the dictionary
print(x)
x = phone.values
y = phone.keys

print(x)
print(y)

# change values

# you can also chanmge values of a specific item by referring to its key name
house = {
    "type": "bungalow",
    "color": "brown",
    "rooms": 3
}
print(house)

house["color"] = "white"
print(house)

# update dictionary
# the update method will update the dictionary with the items from the given argument
# the argument must be a dictuionary, or an iterable object with key: value pairs
# update the rooms of the house by using the update method

house.update({"rooms":5})
print(house)

# removing items
# there are several methods to remove items from a dictiopnary

# the pop() method removes the item with the specified key name:
house.pop("type")
print(house)

# the popitem() method removes the last inserted item
house.popitem()
print(house)

# the del keyword removes the item with thwe specified key name:
print(vehicle)
del vehicle["brand"]
print(vehicle)

# the del keyword can also delete a dictionary completely
# del vehicle
# print(vehicle)


# the clear() method
# the clear method empties the dictionary: 
print(car)
car.clear()
print(car)

# copy a dictionary
name = "larry"
myname = name
print(name)
print(myname)

names = ["Daniella", "Adeola", "Chigozie", "Farouk"]
mystudents = names
print(mystudents)

thisdict = {
    "name": "Daniella",
    "courses": ["HTML", "CSS", "JAVASCRIPT", "PYTHON"]
}

mydict = thisdict
print(mydict)

# another method is using the copy() method
mydict2 = thisdict.copy()
print(mydict2)

thisdict["courses"].append("MYSQL")
print(thisdict)
print(mydict)
print(mydict2)

# Nested Dictionary

myfamily = {
    "child1": {
        "name": "Daniella",
        "year": 2009
    },

    "child2": {
        "name": "Adeola",
        "year": 2008
    },

    "child3": {
        "name": "Chigozie",
        "year": 2007
    },

    "child4": {
        "name": "Farouk",
        "year": 2006
    }
}

print(myfamily)

child1 = {
        "name": "Daniella",
        "year": 2009
}

child2 = {
        "name": "Adeola",
        "year": 2008
}

child3 = {
        "name": "Chigozie",
        "year": 2007
}

child4 = {
        "name": "Farouk",
        "year": 2006
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
    "child4": child4
}

# access items in nested dictionaries
print(myfamily["child2"]["name"])