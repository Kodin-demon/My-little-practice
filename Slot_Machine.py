import random

def spin_row():
    symbols = ["🥥","🍋","🍓","🍒","🍑"]

    return [random.choice(symbols) for _ in range(3)]

def display_row(row):
    print("______________")
    print(" | ".join(row))
    print("______________")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🥥':
            return bet * 2.5
        elif row[0] == '🍑':
            return bet * 1.25
        elif row[0] == '🍓':
            return bet * 2
        elif row[0] == '🍒':
            return bet * 1.75
        elif row[0] == '🍋':
            return bet * 3
    if row[0] == row[1] == '🍒' or row[1] == row[2] == '🍒' or row[0] == row[2] == '🍒':
        return bet * 0.75

    return 0

def main():
    balance = 50
    print("______________________________")
    print("Welcome to gamblers Heaven")
    print("______________________________")
    print("Possible Symbols: 🥥🍋🍓🍒🍑")
    print("______________________________")

    while balance > 0:
        print(f"Current balance: {balance:.2f} €")
        bet = input("Enter amount you want to bet: ")

        if not bet.isdigit():
            print("Please enter a valid number!!!")
            continue

        bet = float(bet)

        if bet > balance:
            print("You can not bet more than you have!!!")
            continue

        if bet <= 0:
            print("Invalid amount!!!")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning . . .\n")
        display_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won {payout:.2f} €")
        else:
            print("You lost your bet")

        balance += payout

        play_again = input("Would you like to play again? |Y/N| ").upper()
        if play_again != 'Y':
            break

        print(f"Game finished! Your final balance is {balance} €")

if __name__ == '__main__':
    main()