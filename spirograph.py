from turtle import Turtle, Screen
import random


def generate_random_color_rgb():
    """
    Generates a random color in RGB format.
    Returns:
        tuple: RGB color tuple (red, green, blue) with values in the range [0, 1].
    """
    red = random.uniform(0, 1)
    green = random.uniform(0, 1)
    blue = random.uniform(0, 1)

    return red, green, blue


# Set up the turtle graphics window
screen = Screen()
screen.bgcolor("black")

# Create a turtle for drawing
spirograph = Turtle()
spirograph.shape("turtle")
spirograph.speed(0)

# Draw a spirograph pattern
for i in range(36):  # 36 outer rotations
    # Add rotating circles
    for j in range(10):  # 10 inner rotations in each outer rotation
        # Change color for each circle
        spirograph.color(*generate_random_color_rgb())  # Use the new function
        spirograph.circle(100)
        spirograph.right(10)

    # Move the spirograph to the next position
    spirograph.penup()
    spirograph.forward(100)
    spirograph.pendown()

# Close the turtle graphics window on click
screen.exitonclick()
