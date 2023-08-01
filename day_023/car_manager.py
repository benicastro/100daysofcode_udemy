"""
CarManager Class - represents the passing cars in the game
"""

# Import needed modules
from turtle import Turtle
import random

# Declare global variable or constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION_X = 300


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        """This function creates cars."""
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(STARTING_POSITION_X, random.randint(-250, 250))
        new_car.move_distance = STARTING_MOVE_DISTANCE
        self.all_cars.append(new_car)

    def drive_cars(self):
        """This function makes the car move."""
        for car in self.all_cars:
            car.backward(self.moving_distance)

    def increase_speed(self):
        """This function increases the move speed of a car if the player reaches a higher level."""
        self.moving_distance += MOVE_INCREMENT
