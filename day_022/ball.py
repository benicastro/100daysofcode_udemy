# Import needed module
from turtle import Turtle
import random

# Declare constants
SHAPE = "circle"
COLOR = "white"
WIDTH = 20
HEIGHT = 20
POSITION = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.turtlesize(stretch_wid=WIDTH/20, stretch_len=HEIGHT/20)
        self.goto(POSITION)
        self.x_inc = 3 * random.choice([-1, 1])
        self.y_inc = 3 * random.choice([-1, 1])
        self.move_speed = 0.001

    def move(self):
        """This function makes the ball move."""
        new_x = self.xcor() + self.x_inc
        new_y = self.ycor() + self.y_inc
        self.goto(new_x, new_y)

    def bounce(self):
        """This function makes the ball change its direction upon hitting a wall."""
        self.y_inc *= -1

    def hit(self):
        """This function makes the ball change its direction upon hitting a paddle."""
        self.x_inc *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """This function takes the ball back to its initial position."""
        self.home()
        self.hit()
