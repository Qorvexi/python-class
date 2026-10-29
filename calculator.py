symbols = input("Pick one: +, -, *, /, %, **: ")
no_1 = int(input("pick a number: "))
no_2 = int(input("pick a number: "))

if symbols == "+":
    result = no_1 + no_2
elif symbols == "-":
    result = no_1 - no_2
elif symbols == "*":
    result = no_1 * no_2
elif symbols == "/":
    result = no_1 / no_2
elif symbols == "%":
    result = no_1 % no_2
elif symbols == "**":
    result = no_1 ** no_2
else:
    print(f"{symbols} is not a symbol")
print(result)

print("The sum of 6 and 7 is 13")
print("The difference of 6 and 7 is -1")
print("The product of 6 and 7 is 42")
print("The quotient of 6 and 7 is 0.857")
print("The modulus of 6 and 7 is 6")
print("The exponent of 6 and 7 is 279936")
