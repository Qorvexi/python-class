# # PYTHON input() FUNCTION
# # The input() function allows a program to receive information from the user while it is running.
# # SYNTAX:
# variable_name = input("Message to the user")
# name = input("Enter name:")
# print(name)
# print("hello" + name)
# print("Good morning " + name + ", Welcome to today's class. How are you feeling?")
# age = input("Enter age: ")
# fav_food = input("Enter your favourite food: ")
# # NOTE: the input() function always returns a string, even if the user enters a number
# print("My name is " + name + ". I am " + age + " years old. My favourite food is " + fav_food + ".")
# score = input("Enter score: ")
# score = input("Enter score: ")
# print(score)
# type(score)
# # converting input to numbers
# # using int()
# score = int(input("Enter score: "))
# print(score)
# print(type(score))
# # for decimal numbers use float
# # ask the user for height and convert it to float then print the value and data type
# height = float(input("Enter height: "))
# print(height)
# print(type(height))
student_name = input("Enter name")
student_age = input("Enter age:")
course = input("Enter course: ")
print("\n==== Student Details =====")
print("Name: ", student_name)
print("Age: ", student_age)
print("Course: ", course)
