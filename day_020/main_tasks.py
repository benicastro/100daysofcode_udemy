"""
Snake Game by Benedict Castro | benedict.zcastro@gmail.com
"""

# Import needed modules ######################################################################################################
from turtle import Screen
from snake import Snake
import time
import random

# Configure screen properties ################################################################################################
WIDTH = 600
HEIGHT = 600
BG_COLOR = "black"

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title("Milyastroc's Snake Game")
screen.tracer(0)

# Create a Snake body ########################################################################################################
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in STARTING_POSITIONS:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)

# Animate the Snake segments on Screen #######################################################################################
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
#
# for position in STARTING_POSITIONS:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# # Create a variable which indicates if the game is running
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg_num in range(len(segments)-1, 0, -1):
#         segments[seg_num].goto(x=segments[seg_num-1].xcor(), y=segments[seg_num-1].ycor())
#     segments[0].forward(20)

# Create a Snake Class & Move to OOP ##########################################################################################
# snake = Snake()
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#     snake.move()

# Control the Snake with a keypress ###########################################################################################
snake = Snake()

# Make the screen listen to keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()





# Prevent the window from closing without user intervention
screen.exitonclick()
