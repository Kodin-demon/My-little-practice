# attempt to create a program to calculate fibonach sequence

# creating empty variables for later use

first_num = 0
second_num = 1
fibonaci = []
request = int(input("Enter max value number you wish to see: "))

# main part that does the calculation

while first_num < request:
    fibonaci.append(first_num)
    summe = first_num + second_num
    first_num = second_num
    second_num = summe

# A way to display the results of previos calculation

for num in fibonaci:
    print(num, end=" ")

