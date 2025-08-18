def display_balance(balance):
    print(f"Your balance is {balance:.2f} €")

def deposit():
    deposit_amount = float(input("How much would you like to deposit: "))

    if deposit_amount <= 0:
        print("That is not valid amount!!!")
        return 0
    else:
        return deposit_amount

def withdraw(balance):
    withdraw_amount = float(input("How much would you like to withdraw: "))

    if balance < withdraw_amount:
        print("You dont have that much money!!!")
        return 0
    elif withdraw_amount < 0:
        print("Withdraw amount should be greater than 0 !!!")
    else:
        return withdraw_amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Welcome to your Bank Program")
        print("1) Display Balance")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Close Program")

        choice = input("Please choose one of the options //1-4//: ")

        match choice:
            case "1":
                display_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("Chosen option is not valid!!!")

    print("Thanks for using out App, have a good day")

if __name__ == '__main__':
    main()