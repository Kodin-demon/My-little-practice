# this programm is expected to create any form with 4 90° angles

collums = int(input("Select number of collums: "))
rows = int(input("Select number of rows: "))
fillament = input("Select your fillament: ")

for x in range(collums):
    for y in range(rows, 0, -1):
        print(fillament, end="")
    print()