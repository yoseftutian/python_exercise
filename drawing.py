from turtle import Turtle, Screen

# Create a turtle
pen = Turtle()
screen = Screen()


# Function to move the turtle forward
def draw_forward():
    pen.forward(10)


# Function to move the turtle backward
def draw_backward():
    pen.backward(10)


# Function to turn the turtle to the left
def draw_left():
    pen.left(10)


# Function to turn the turtle to the right
def draw_right():
    pen.right(10)


# Function to clear the screen and reset the turtle to the center
def clear_screen():
    pen.clear()
    reset_position()


# Function to reset the turtle position to the center of the screen
def reset_position():
    pen.penup()  # Lift the pen
    pen.goto(x=0, y=0)  # Move to the center of the screen
    pen.pendown()  # Put the pen down


# Listen for keyboard input
screen.listen()

# Assign keys to actions
screen.onkey(key="w", fun=draw_forward)
screen.onkey(key="s", fun=draw_backward)
screen.onkey(key="a", fun=draw_left)
screen.onkey(key="d", fun=draw_right)
screen.onkey(key="c", fun=clear_screen)

# Start the main event loop
screen.mainloop()
