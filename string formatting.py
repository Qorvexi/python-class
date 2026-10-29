# # let's say we have a variable called "name" with a user name in it, and you would like to print(out greeting to that user.)

# # This print Hello, Larry!
# name = "Larry"
# age = 22
# print("Hello, ", name)
# print("Hello " + name + " i am " + str(age) + " years old")

# print("Hello, %s!" %name)
# print("My name is %s" %name)

# # Multiple varianles formatting
# print("%s is %d years old" %(name, age))

# # to use two or more argument specifiers, use a tuple(parenthesis):

# # Example: print out "John is 23 years old."
# name = "John"
# age = 23

# print("%s is %d years old." %(name, age))

# # lists
# mylist = [1, 2, 3]
# print("A list: %s" %mylist)
# # %s - string
# # %d - integers
# # %f - float
# # %.<number of digits>f - floating point numbers with a fixed amount of digits to the right of the dot

# gpa = 12.568
# print("My gpa is %.2f" %gpa)
# astring = "hello world"
# astring2 = "hello world"

# print("single quotes are '' ")
# print('single quotes are '' ')
# print("Don't")
# print('Don\'t')

# # string methods
# # len() returns the number of characters in a string

# print(len(astring))
# print(len("Larry Thomzy"))

# # index: it returns the number of characters in a string

# print(astring.index("o"))
# print(astring.index("o", 5))

# # count : it counts and returns how many times a character appears

# astring = "Hello world!"
# print(astring[3:7])
# print(astring[3:7:2])
# print(astring[::-1])

# print(astring.upper())
# print(astring.lower())

# print(astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))

# # split

# lettersplit = list(astring)
# print(lettersplit)

# # using strip()
# # removes extra spaces from the beginning and end of a string

# print("Before strip:", astring)
# print("After strip:", astring.strip())

# # removes specific characters from both ends of a string
# text = "...Hello World!!!..."
# print(text.strip(".!"))

# # exercise 1: email valisdator
# # check if a string looks like an email (contains "@" and ends with .com)
# email = input("Enter your email: ")
# if "@" in email and email.endswith(".com"):
#     print("Valid email")
# else:
#     print("Invalid email")
# # exercise 2: password length checker
# # check if a password has at least 8 characters and contains both uppercase and lowercase letters
# password = input("Enter your password: ")
# has_upper = any(ch.isupper() for ch in password)
# has_lower = any(ch.islower() for ch in password)
# # has_digit = any(ch.is_digit() for ch in password)
# if len(password) >= 8 and has_upper and has_lower:
#     print("Strong pass")
# else:
#     print("Weak password")

# # method 2
# if len(password) >= 8 and password != password.upper() and password != password.lower():
#     print("Strong password")
# else:
#     print("Weak password")

# # exercise 3: word counter
# # ask for a sentence and print each word with its character count===================================================================================================================================================================================================================================================================================================================================================
# sentence = input("Enter a sentence")
# sent = list(sentence) 
# for x in sent:
#     print(x, len(x))
# # exercise 4: reverse and check
# # reverse a word and check if it has a palindrome (reads the same backwards)
# p_word = input("Enter word: ")
# if p_word[::-1] == p_word:
#     print("Palindrome")
# else:
#     print("Go to school")

# excersise 5: attendance list formatter 
# convert a list of names into a formatted  string for display
attendance = ["Farouk", "His father", "Adeola", "His father", "Wande", "His father"]
print(attendance[0])
print(attendance[1])
print(attendance[2])
print(attendance[3])
print(attendance[4])
print(attendance[5])
