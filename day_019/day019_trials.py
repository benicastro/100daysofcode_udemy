# from turtle import Turtle, Screen
#
# emi = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     emi.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

###############################################################################################################################
# Etch-A-Sketch Program ###

# Import needed modules
from turtle import Turtle, Screen

# Declare classes
emi = Turtle()
screen = Screen()

# Define functions for movement


def move_forwards():
    emi.forward(10)


def move_backwards():
    emi.backward(10)


def rotate_clockwise():
    emi.setheading(emi.heading()-5)


def rotate_counter_clockwise():
    emi.setheading(emi.heading()+5)


def clear():
    emi.clear()
    emi.penup()
    emi.home()
    emi.pendown()


# Configure screen
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

