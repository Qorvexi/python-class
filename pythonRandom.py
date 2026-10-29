import random

from calculator import result

# the random module allows python to generate random values

# random.randit()
# generates a random integer within a range
num = random.randint(1,10)
print(num)

# random.choice()
# selects a random item from a list
fruits = ["apple", "banana", "cherry"] # list
print(random.choice(fruits))

# random.random()
# generates a random decimal number between 0 and 1
print(random.random())

# random.shuffle()
# shuffles all items in a list
cards = ["king", "queen", "jack", "diamond"]
random.shuffle(cards)
print(cards)

# random.uniform()
# generates a random decimal number between two values
print(random.uniform(1,10))

# mini game
result = random.choice(["heads", "tails"])
print(result)

# guessing game
print("*********************************")
print("NUMBER GUESSING GAME")
print("*********************************")
number = random.randint(1,20)
guess = int(input("Enter the lucky number: "))
if guess == number:
    print("You win!")
else:
    print("You lose!")
    print("The number was: " + number)