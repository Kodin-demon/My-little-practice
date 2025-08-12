# dictionary = {key:value}
# .get - retrives a value from a key
# .update - add a new key:value or update existing one
# .pop - removes key.value
# .popitem - removes latest key:value
# .clear - clears dictionary
# .keys - gets keys from dictionary as a list
# .values - gets values
# .items - returns key:value as 2D Tuple

menu = {"popcorn": 8.00,
        "candy": 6.50,
        "soda": 5.00,
        "chips": 7.50}

cart = []
total = 0

print("_-_-_-_-_-_-MENU-_-_-_-_-_-_")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f} €")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

while True:
    food = input("Select an item (Q to quit) ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("_-_-_-_-_-_Your Order_-_-_-_-_-_")
for item in cart:
    total += menu.get(item)
    print(item)

print("_-_-_-_-_-_Your Total_-_-_-_-_-_")
print(f"Your total is {total:.2f} €")
