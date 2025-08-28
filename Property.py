# That all is still look a bit confusing about how and where I can implement this

class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width: .2f} m"

    @property
    def height(self):
        return f"{self._height: .2f} m"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width cannot be equal or lower that zero!!!")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height cannot be equal or lower that zero!!!")

    @width.deleter
    def width(self):
        del self._width
        print("Width was deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height was deleted")


rectangle = Rectangle(7,5)

print(rectangle.width)
print(rectangle.height)