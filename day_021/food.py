# Import needed module ########################################################################################################
from turtle import Turtle
import random

# Declare constant(s) #########################################################################################################
SHAPES = ["turtle", "circle", "square", "triangle"]


# Create Food class ###########################################################################################################
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """This function resets the position of the food into a random location."""
        self.shape(random.choice(SHAPES))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
