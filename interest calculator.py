# Python interest calculator

#these variables should all be less than a zero (0)
sbalance = -1
rate = -1
time = -1

#inputs requests from a user, inputs can not be less than a zero
while sbalance < 0:
    sbalance = float(input("Enter your starting balance: "))
    if sbalance < 0:
            print("Your starting balance cant be less than a zero!")

while rate < 0:
    rate = float(input("Enter your interest rate: "))
    if rate < 0:
            print("Your interest rate cant be less than a zero!")

while time < 0:
    time = float(input("Enter your time in years: "))
    if time < 0:
            print("Your time cant be less than a zero!")

#the calculator with a simple formula
ebalance = round((sbalance * pow(1 + (rate / 100), time)), 2)

print(f"Your balance after {time} years with {rate}% interest rate is {ebalance:,}€")