# Import needed module ########################################################################################################
from turtle import Turtle

# Declare constant(s) #########################################################################################################
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Create Snake class ##########################################################################################################
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """This function creates the initial snake body."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """This function adds a new segment to the snake body."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """This function adds a new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake based on user commands."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(x=self.segments[seg_num - 1].xcor(), y=self.segments[seg_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn the snake head upwards."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the snake head upwards."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the snake head upwards."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the snake head upwards."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

