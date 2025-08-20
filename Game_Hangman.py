import random

words = ("APPLE", "ORANGE", "BANANA", "COCONUT", "MANGO", "TOMATO")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")
               }

def display_man(wrong_guesses):
    print("_-_-_-_-_-_-_-_-")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("_-_-_-_-_-_-_-_-")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letter:
            print(f"Letter [{guess}] is already guessed")
            continue

        guessed_letter.add(guess)

        if guess in  answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulation, you won")
            print(f"You guessed wrong {wrong_guesses} times")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Sorry, you lost")
            print(f"You guessed wrong {wrong_guesses} times")


if __name__ == '__main__':
    main()