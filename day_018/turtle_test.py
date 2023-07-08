from turtle import Turtle, Screen
import random

# timmy_the_turtle = Turtle()
#
# turtle_shape = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
# shape = random.choice(turtle_shape)
# timmy_the_turtle.shape(shape)
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
#
# screen = Screen()
# screen.exitonclick()

###############################################################################################################################
# Turtle Challenge 1 - Draw a Square

# emi = Turtle()
# emi.shape("turtle")
#
# for _ in range(4):
#     emi.forward(100)
#     emi.right(90)
#
# screen = Screen()
# screen.exitonclick()

###############################################################################################################################
# Turtle Challenge 2- Draw a Dashed Line

# emi = Turtle()
#
# for _ in range(20):
#     emi.pendown()
#     emi.forward(5)
#     emi.penup()
#     emi.forward(5)
#
# screen = Screen()
# screen.exitonclick()

###############################################################################################################################
# Turtle Challenge 3 - Drawing Different Shapes

# emi = Turtle()
# colors = ["cornflower blue", "medium turquoise", "medium spring green", "deep sky blue", "gold",
#           "maroon", "plum", "medium slate blue"]
# random.shuffle(colors)
#
# for i in range(3, 11):
#     angle = 360 / i
#     emi.color(colors.pop())
#     for j in range(i):
#         emi.forward(100)
#         emi.right(angle)
#
# screen = Screen()
# screen.exitonclick()
###############################################################################################################################
# Turtle Challenge 4 - Generate a Random Walk

# emi = Turtle()
# emi.pensize(5)
# emi.speed(7)
#
# colors = ["cornflower blue", "medium turquoise", "medium spring green", "deep sky blue", "gold",
#           "maroon", "plum", "medium slate blue"]
# angles = [90, 180, 270, 360]
#
# for _ in range(200):
#     emi.forward(30)
#     emi.color(random.choice(colors))
#     emi.setheading(random.choice(angles))
#
# screen = Screen()
# screen.exitonclick()
###############################################################################################################################
# from turtle import colormode
# emi = Turtle()
# colormode(255)
#
# emi.pensize(5)
# emi.speed(7)
# angles = [90, 180, 270, 360]
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tuple_color = (r, g, b)
#     return tuple_color
#
#
# for _ in range(200):
#     emi.forward(30)
#     emi.color(random_color())
#     emi.setheading(random.choice(angles))
#
# screen = Screen()
# screen.exitonclick()
###############################################################################################################################
# Turtle Challenge 5 - Draw a Spirograph
from turtle import colormode

emi = Turtle()
colormode(255)

emi.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple_color = (r, g, b)
    return tuple_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        emi.color(random_color())
        emi.circle(100)
        emi.setheading(emi.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
###############################################################################################################################
