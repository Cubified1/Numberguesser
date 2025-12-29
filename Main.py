import random
import time

Difficulty = input("What difficulty would you like to guess? Easy, Medium, Hard: ").lower()



if Difficulty == "easy":
    Correct_Number = random.randint(1, 50)

elif Difficulty == "medium":
    Correct_Number = random.randint(1, 100)

else:
    Correct_Number = random.randint(1, 1000)



if Difficulty == "easy":
    user_guess = int(input("guess the number from 1 to 50: "))

elif Difficulty == "medium":
    user_guess = int(input("guess the number from 1 to 100: "))

else:
    user_guess = int(input("guess the number from 1 to 1000: "))

while not user_guess == Correct_Number:
    print("wrong guess, try again")
    quit = input("Do you want to quit? (y/n): ")
    if quit == "y":
        break
    else:
        user_guess = int(input("guess the number from 1 to 1000: "))




if user_guess == Correct_Number:
    print("Correct")


time.sleep(5)
