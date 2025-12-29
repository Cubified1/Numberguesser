import random
import time


Correct_Number = random.randint(1, 1000)

user_guess = int(input("guess the number from 1 to 1000: "))

while not user_guess == Correct_Number:
    print("wrong guess, try again")
    user_guess = int(input("guess the number from 1 to 1000: "))

if user_guess == Correct_Number:
    print("Correct")


time.sleep(5)
