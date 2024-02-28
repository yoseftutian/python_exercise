import math


class Shape():
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def display_info(self):
        print(f" the information is, color is: {self.color}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def display_info(self):
        super().display_info()
        print(f" radios is:{self.radius} area is:{self.area()}")


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display_info(self):
        print(f" the information about shape is: color is: {self.color} length is:{self.length}"
              f" width is:{self.width}area is:{self.area()}")


rte = Shape("blue")
rte.display_info()
# print(rte.display_info())
ghy = Circle("green", 67)
ghy.display_info()
