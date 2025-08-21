class Car:
    # ^^can be stored in a separate file to organize
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        #^^ it really quite selfish

    def steering(self):
        print(f"You drive the {self.color} {self.model}")

    def brakes(self):
        print(f"You stopped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Ford",1993, "dark blue", False)
car2 = Car("Mazda",2006, "red", True)
#           ^^and this really looks like a funktion, but it is not

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)
#^^doing all that with a funktion, that for class is called method
car1.describe()
car1.brakes()
car2.steering()
