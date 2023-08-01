"""
Player Class - represents the player's sprite in the game.
"""

# Import needed modules
from turtle import Turtle

# Declare global variables or constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.go_to_start()

    def move(self):
        """This function lets the player move"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """This function resets the position of the turtle to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """This function returns true if the player reached the designated finish line."""
        return self.ycor() > FINISH_LINE_Y
