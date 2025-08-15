# function = a block of reusable code
#            placing () after the function to invoke it

def display_invoice(username, amount, due_date):
    #               ^^ You can also put parameters inside that you can use //also called arguments//
    print(f"Good day {username}")
    print(f"Your bill of {amount}€ is due: {due_date}")

display_invoice("Alfred", 459.99, "30. August 2025")
#               ^^ But you have to be precise in which order you put them in. Unless you specify each one

# return = statement used to end a funktion
#          and send a result back to the caller

def add(num1, num2):
    ans = num1 + num2
    return ans

def subtract(num1, num2):
    ans = num1 - num2
    return ans

def multiply(num1, num2):
    ans = num1 * num2
    return ans

def divide(num1, num2):
    ans = num1 / num2
    return ans

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("koDin", "dark")

print(full_name)