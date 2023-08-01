# Import needed module
from turtle import Turtle

# Declare constants
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 67, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """This functions adds a point to the left player."""
        self.l_score += 1

    def r_point(self):
        """This functions adds a point to the right player."""
        self.r_score += 1

