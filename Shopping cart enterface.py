# my little programm to help with organizing your shopping lists
from typing import ItemsView

items = []
prices = []
# quantity = []
total = 0

# gathering info about your shopping prioritys
while True:
    item = input("Enter an item (e to End): ")
    if item.lower() == "e":
        break
    else:
        price = float(input(f"Enter a price of a {item}: €"))
        # amount = int(input(f"Enter an amount of a {item}: "))
        items.append(item)
        prices.append(price)
        # quantity.append(amount)

# main part where magic happens
print("_____Your cart_____")

# getting items from a list
for item in items :
    print(item, end=" ")
print()

for price in prices:
    print(price, end="€ ")
    total += price
print()

print(f"Your total is {total}€")
