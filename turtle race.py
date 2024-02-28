# Importing Libraries
from turtle import Turtle, Screen
from tkinter import messagebox
import random

# Setting up the Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=400)

# Creating Turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):
    jki = Turtle(shape="turtle")
    jki.shapesize(1, 1.2)
    jki.color(colors[i])
    jki.penup()
    jki.goto(x=-250, y=-100 + i * 45)  # Initial position for each turtle
    turtles.append(jki)

# Getting User Bet
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? (enter a color): ")

# Race Simulation
race_on = True

while race_on:
    for jki in turtles:
        # Moving the turtles forward
        distance = random.randint(a=1, b=20)
        jki.forward(distance)

        # Checking if any turtle has reached the finish line
        if jki.xcor() > 265:
            race_on = False
            winning_color = jki.pencolor()

            # Displaying result in a pop-up window
            if winning_color == user_bet:
                messagebox.showinfo(title="Game Over", message=f"You've won! The {winning_color} turtle is the winner.")
            else:
                messagebox.showinfo(title="Game Over",
                                    message=f"You've lost! The {winning_color} turtle is the winner.")

            break

# Ending the Program
screen.exitonclick()
