print("Hello there my friend")

name = input("What is your name: ")
print(f"Nice to meet you {name}")

age = float(input("How old are you: "))

if age >= 60:
    print("You have lived for very long time")
    answer = input("is there anything you would like to tell:")
    if answer == "":
        print("Oh, that a shame to hear that")
    else:
        print(f"That is nice to know that {answer} is important")
elif age >= 20:
    print("Wow you are quite old")
elif age <= 16:
    print("You are still young")
else:
    print("That wasnt the right age you tipped in")