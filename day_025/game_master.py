"""
GameMaster Class - manages the overall mechanics of the US States Quiz Game
"""

# Import needed modules
from turtle import Turtle

# Declare constants/global variables
ALIGNMENT = "center"
FONT = ("Courier", 11, "normal")


class GameMaster(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # Keep track of score
        self.correct_answers = []  # Keep track of correct answers

    def create_background(self, image_file):
        """This function takes in an image file and makes it the background of the screen."""
        self.shape(image_file)

    def increase_score(self, answer):
        """This function adds a point to the user score for every correct answer and then adds the answer to a list."""
        self.score += 1
        self.correct_answers.append(answer)

    def display_answer(self, x, y, answer):
        """This function takes in the x and y coordinates of the state, and then writes the state on the screen in that location."""
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f"{answer}", align=ALIGNMENT, font=FONT)







