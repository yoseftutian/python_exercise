class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return int(self.width * self.height)

    def calculate_perimeter(self):
        return int(2 * (self.width + self.height))


# Taking input for width and height
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

# Creating a Rectangle object
my_rectangle = Rectangle(width, height)

# Calculating and printing the area
area = my_rectangle.calculate_area()
print(f"Area of the rectangle: {area}")

# Calculating and printing the perimeter
perimeter = my_rectangle.calculate_perimeter()
print(f"Perimeter of the rectangle: {perimeter}")
