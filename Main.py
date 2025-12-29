import random
import time

Difficulty = input("What difficulty would you like to guess? Easy, Medium, Hard: ")


if Difficulty == "Easy":
    Correct_Number = random.randint(1, 50)

elif Difficulty == "Medium":
    Correct_Number = random.randint(50, 100)

else:
    Correct_Number = random.randint(100, 1000)


if Difficulty == "Easy":
    user_guess = int(input("guess the number from 1 to 50: "))

elif Difficulty == "Medium":
    user_guess = int(input("guess the number from 1 to 100: "))

else:
    user_guess = int(input("guess the number from 1 to 1000: "))

while not user_guess == Correct_Number:
    print("wrong guess, try again")
    user_guess = int(input("guess the number from 1 to 1000: "))

if user_guess == Correct_Number:
    print("Correct")


time.sleep(5)
