from abc import ABC,abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 3.14 * self.side ** 2

class Cake:
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(3), Square(2), Cake("Strawberry",1)]

for shape in shapes:
    print(f"{shape.area()} m²")