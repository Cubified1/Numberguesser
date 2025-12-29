import random
import time

Difficulty = input("What difficulty would you like to guess? Easy, Medium, Hard: ").lower()
Incorrect_Guesses = 0
Close_Counter = 0

print("Welcome to Number Guess Game")

if Difficulty == "easy":
    Correct_Number = random.randint(1, 50)

elif Difficulty == "medium":
    Correct_Number = random.randint(1, 100)

else:
    Correct_Number = random.randint(1, 1000)
print(Correct_Number)


if Difficulty == "easy":
    user_guess = int(input("guess the number from 1 to 50: "))

elif Difficulty == "medium":
    user_guess = int(input("guess the number from 1 to 100: "))

else:
    user_guess = int(input("guess the number from 1 to 1000: "))

while not user_guess == Correct_Number:
    print("wrong guess, try again")
    Incorrect_Guesses += 1
    if Incorrect_Guesses == 1:
        print(f"you've guessed wrong {Incorrect_Guesses} time")
    else:
        print(f"you've guessed wrong {Incorrect_Guesses} times")
    quit = input("Would you like to quit? (y/n): ").lower()

    while not quit in ("n", "y"):
        print("please enter a y or n")
        quit = input("Would you like to quit? (y/n): ").lower()


    if quit == "y":
        for Close_Counter in range(1, 3):
            print(f"closing in {Close_Counter}")
            time.sleep(1)
        break



    if Difficulty == "easy":
        user_guess = int(input("guess the number from 1 to 50: "))
    elif Difficulty == "medium":
        user_guess = int(input("guess the number from 1 to 100: "))
    else:
        user_guess = int(input("guess the number from 1 to 1000: "))




if user_guess == Correct_Number:
    print("Correct")
    for Close_Counter in range(1, 3):
        print(f"closing in {Close_Counter}")
        time.sleep(1)
