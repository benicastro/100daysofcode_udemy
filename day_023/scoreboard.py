"""
Scoreboard Class - represents the scoreboard for the game and shows the current game level
"""

# Import needed modules
from turtle import Turtle

# Declare constants
FONT = ("Courier", 17, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function updates the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """This function increases the level."""
        self.level += 1
