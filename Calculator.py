# my little project to make calculator for basic functions
import math

operator = input("Please choose your math operator (+ - * / ^): ")

number1 = float(input("Please enter your 1st number: "))
number2 = float(input("Please enter your 2nd number: "))

if operator == "+":
    result = round(number1 + number2,2)
    print(f"Your answer is {result}")
elif operator == "-":
    result = round(number1 - number2,2)
    print(f"Your answer is {result}")
elif operator == "*":
    result = round(number1 * number2,2)
    print(f"Your answer is {result}")
elif operator == "/":
    result = round(number1 / number2,2)
    print(f"Your answer is {result}")
elif operator == "^":
    result = round(pow(number1,number2),2)
    print(f"Your answer is {result}")
else:
    print("That is NOT valid operator")

