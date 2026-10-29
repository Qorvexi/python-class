# PYTHON OPERATOR
# An operator is a symbol that tells Python to perform an operation on one or more values.
# TYPES OF OPERATOR
# Python has several types of operators:
# 1. Arithmetic operator
# 2. Assignment operator
# 3. Comparison operator
# 4. Logical operator
# 5. Membership operator
# 6. Identity operator
#######################################################################################################################################################
# 1. ARITHMETIC OPERATORS
# ADDITION (+)
print(3 + 6)
print(1 + 2)
print(3 + 4)
print(5 + 8)
print(6 + 7)
# SUBTRACTION
print(6 - 3)
print(2 - 1)
print(4 - 3)
print(8 - 5)
print(7 - 6)
# MULTIPLICATION
print(6 * 3)
print(2 * 1)
print(4 * 3)
print(8 * 5)
print(7 * 6)
# DIVISION (/)
print(6 / 3)
print(2 / 1)
print(4 / 2)
print(8 / 4)
print(10 / 5)
# FLOOR DIVISION
print(6 // 3)
print(2 // 1)
print(4 // 2)
print(8 // 4)
print(10 // 5)
# MODULUS / REMAINDER
print(6 % 3)
print(2 % 1)
print(4 % 2)
print(8 % 4)
print(10 % 5)
# EXPONENT (POWER)
print(6 ** 3)
print(2 ** 1)
print(4 ** 2)
print(8 ** 4)
print(10 ** 5)
 # 2. ASSIGNMENT OPERATOR
x = 23
# Compound assignment
# add and assign
x += 2
# subtract and assign
x -= 2
# multiply and assign
x *= 2
# divide and assign
x /= 2
# 3. COMPARISON OPERATORS
# Equal to
print(5 == 5)
print(6 == 3)
# Not equal to
print(7 != 6)
print(9 != 9)
# Greater than
print(7 > 6)
print(6 > 7)
# Less than
print(6 < 7)
print(7 < 6)
# Greater than or equal to
print(7 >= 7)
print(6 >= 7)
# Less than or equal to
print(7 <= 7)
print(7 <= 6)
False
# 4. LOGICAL OPERATORS
# And - returns true only if both conditions are true
print(10 > 5 and 8 > 3)
# Or - returns true if at least one of the conditions is true
print(10 > 5 and 8 < 3)
# Not - reverses a boolean value
print(not True)
print(not False)
print(not 10 > 5)
print(not 10 < 5)
# 5. MEMBERSHIP OPERATORS - These check whether a value exists in a sequence.
course = "Python"
print("y" in course)
print("Y" in course)
print("p" in course)
print("P" in course)
# Not in
print("c" not in course)
print("th" not in course)
# EXERCISE
program = "JavaScript"
# check for java, JA, Script, script, VA, ja
print("java" in program)
print("JA" in program)
print("Script" in program)
print("script" in program)
print("VA" in program)
print("ja" in program)
# 6. IDENTITY OPERATORS - are used to check whether two variables refer to the same object in memory, not just whether they have the same value.
# is
a = 3
b = 3
print(a is b)
a = [7, 8, 9]
b = [7, 8, 9]
print(a is b)
# When should you use is
value = None
print(value is None)
# OPERATOR PRESIDENCE - Python follows the same order as mathematics
# multiplication before addition
print(2 + 3 * 4)
# use parenthesis to change the order
print((2 + 3) * 4)
# Mini project
# Ask the user to enter first number and second number
# convert to number and store it in a variable
# add (sum), minus (difference), divide (quotient), multiply (product), remainder, exponent both values while displaying the answer to the user
# Example: The sum of ...... and ......... is ...........
