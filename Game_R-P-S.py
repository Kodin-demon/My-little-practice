import random

options = ("rock", "paper", "scissors")
playing = True

while playing:

    # To reset variables they are placed inside a while loop
    player = None
    computer = random.choice(options)

    #make sure that player enters a valid option
    while player not in options:
        player = input("What is your choice //Rock, Paper, Scissors//: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    #we enter our win conditions and if there is  no match, then player lose
    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    # Asking player if they are willing to play again
    if not input("Play again? (Y/N) ").lower() == "y":
        playing = False

# if not we thank the for playing
print("Thank you for playing!!!")