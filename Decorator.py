
def add_sirup(func):
    def wrapper(*args, **kwargs):
        print("With Syrup of your choosing  🍯")
        func(*args, **kwargs)
    return wrapper
    #             ^^ I have put () in here and couldn't understand why wasn't the code working,
    #                I am so dumb sometimes, hope I won´t do the same mistake one day

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("With a fudge on top          🧱")
        func(*args, **kwargs)
    return wrapper

@add_sirup
@add_fudge
def get_shaved_ice(water_type):
    print(f"Here is your {water_type} crushed ice     🍦")

get_shaved_ice("Vegan")


