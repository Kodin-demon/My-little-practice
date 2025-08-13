# Game of Numbers in Python
import random

print("Hello User, here you can play a game of numbers.")
lowest = int(input("Please select your lowest number: "))
highest = int(input("Then select your highest number: "))
print(f"Now you can guess number between {lowest} and {highest}")

right_num = random.randint(lowest, highest)

guesses = 0
is_running = True

while is_running:

    user_guess = input("Your guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1

        if user_guess < lowest or user_guess > highest:
            print("Your guess is out of guessing range")
            print(f"Guess a number between {lowest} and {highest}")
        elif user_guess < right_num:
            print("Too low, try higher number")
        elif user_guess > right_num:
            print("Too high, try a lower number")
        else:
            print(f"Correct!!! The answer was {right_num}")
            print(f"It took you {guesses} guess/es")
            is_running = False

    else:
        print("Invalid Guess!!!")
        print(f"Guess a number between {lowest} and {highest}")