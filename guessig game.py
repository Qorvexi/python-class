import random

# ==================================Number Guessing Game=================================================
print("*************************")
print("Welcome to the Guess Game")
print("*************************")
attempts = 5
guess = int(input("Guess a number between 1 and 100: "))
number = random.randint(1, 100)
while guess != number:
    guess = int(input(f"Try Again: "))
    if guess == number:
       print("You win!")
       break
    elif guess > number:
       print("NO, you have guessed too high!")
       attempts -= 1
       print("You have " + str(attempts) + " attempts remaining")
    elif guess < number:
       print("NO, you have guessed too low!")
       attempts -= 1
       print("You have " + str(attempts) + " attempts remaining")
    elif guess != number:
       print("You lose!")
       break
    else:
       print("You lose!")


    if attempts == 0:
       print("You lose!")
       break
    else:
       print(number)