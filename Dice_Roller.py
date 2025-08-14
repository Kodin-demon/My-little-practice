import random

# copied from internet: ● ┌ ─ ┐ │ └ ┘
# blueprint for dice
#"┌─────────┐"
#"│         │"
#"│         │"
#"│         │"
#"└─────────┘"

dice_collection = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘" ),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘" ),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘" ),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘" ),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘" ),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘" )
}

dice = []
total = 0
num_of_dice = int(input("How many Dices you would like to roll?"))

for roll in range(num_of_dice):
    dice.append(random.randint(1, 6))

#for die in range(num_of_dice):
#    for line in dice_collection.get(dice[die]):
#        print(line)

for line in range(5):
    for die in dice:
        print(dice_collection.get(die)[line], end= "")
    print()

for amount in dice:
    total += amount

print(f"Your total is: {total}")