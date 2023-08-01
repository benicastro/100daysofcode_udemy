# Import needed module
from turtle import Turtle

# Declare Constants
SHAPE = "square"
COLOR = "white"
WIDTH = 20
LENGTH = 100


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=WIDTH/20, stretch_len=LENGTH/20)
        self.goto(position)

    def move_up(self):
        """This function lets the object move forward."""
        self.forward(20)

    def move_down(self):
        """This function lets the object move backward."""
        self.backward(20)
