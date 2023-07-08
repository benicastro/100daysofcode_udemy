"""
Hirst Painting Project by Benedict Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
import colorgram
from turtle import Turtle, Screen, colormode
import random

# # Extract colors from the image
# colors = colorgram.extract('image.jpg', 20)
#
# colors_rgb = []
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors_rgb.append(color_tuple)

colors_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68),
               (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
               (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]

# Reproduce Hirst painting

# Declare Turtle class
emi = Turtle()
colormode(255)

# Define painting properties
num_dots = 10
spacing = 50
dot_size = 20
x_start = -200
y_start = -200
emi.ht()
emi.penup()
emi.goto(x_start, y_start)

for i in range(num_dots):
    emi.goto(x_start, y_start + spacing*i)
    for j in range(num_dots):
        emi.pendown()
        emi.dot(20, random.choice(colors_list))
        emi.penup()
        emi.forward(50)

# Configure screen
screen = Screen()
screen.exitonclick()
