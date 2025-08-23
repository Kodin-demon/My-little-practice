

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Round(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        # ^^ can be used in constructor not write everything again
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {pow(self.radius, 2) * 3.14}m^2")
        super().describe()
        #^^ and if child class have a method with a same name it will override it
        # to also include the method from a parent class we use same super() funktion

class Rectangle(Shape):
    def __init__(self, color, filled, length):
        super().__init__(color, filled)
        self.length = length

    def describe(self):
        print(f"It is a square with an area of {pow(self.length, 2)}m^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, filled, length, height):
        super().__init__(color, filled)
        self.length = length
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {(self.length * self.height) / 2}m^2")
        super().describe()

circle = Round(color="Blue",filled= True,radius= 3.5)
square = Rectangle(color="Blue",filled= True,length= 5)
triangle = Triangle(color="Blue",filled= True,length= 5, height= 3)

# print(f"{circle.color} {circle.filled} {circle.radius}")
# print(f"{square.color} {square.filled} {square.length}")
# print(f"{triangle.color} {triangle.filled} {triangle.length} {triangle.height}")

circle.describe()
print()
square.describe()
print()
triangle.describe()