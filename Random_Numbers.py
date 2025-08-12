import random

# random.rand<Num_Type>(Lowest, Highest)
# .rand <- random function
# .randINT <- number type, here integer
# .choice - gives a random element of a list
# .shuffle - allows to shuffle a list/tuple
# ^^ seems like I cant assign it to a new variable, cause it return None

low = 0
high = 20
mind = ("Rock", "Paper", "Scissors")
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

choice = random.choice(mind)
random.shuffle(deck)

print(choice)
print(deck)
