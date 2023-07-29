# Import needed module ########################################################################################################
from turtle import Turtle

# Declare constant(s) #########################################################################################################
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


# Create Scoreboard class ###########################################################################################################
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function updates the scoreboard."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """This function adds points to the player score. """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """This function determines whether the game is already over or not."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
