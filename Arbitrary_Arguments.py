# *args     = allows to pass multiple non-key arguments
# **kwargs  = allows to pass multiple keyword-arguments
#           * unpacking operator

def add(*numbers):
    #   ^^ every argument will be stored in a tuple
    total = 0
    for num in numbers:
        total += num
    return total

def display_name(*names):
    for name in names:
        print(name, end= " ")

def print_address(**kwargs):
    #               ^^keyword arguments treated like if they were a dictionary
    for key, value in kwargs:
        print(f"{key}: {value}")

def shipping_label(*args, **kwargs):
    #               ^^ arguments first and then keyword arguments
    #               if not you will get SyntaxError
    for arg in args:
        print(arg, end=" ")
    print()

    if "building" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('building')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('zip')} {kwargs.get('city')} {kwargs.get('state')}")

shipping_label("Undead", "Kodin", "Dark",
               street="Water street", building="4",
               zip="90769", city="Furth", state="Bayern"
               ) # ^^and ofcourse this all can be user inputs, but im lazy for that