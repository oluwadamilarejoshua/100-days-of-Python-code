import turtle
from turtle import Turtle as t, Screen
import random

color_list = [(236, 253, 244), (251, 238, 248), (39, 7, 181), (89, 248, 180), (219, 153, 111), (158, 7, 81), (233, 48, 124), (10, 211, 80), (110, 98, 233), (8, 139, 56), (215, 118, 176), (183, 178, 244), (249, 248, 61), (59, 228, 77), (205, 97, 11), (153, 132, 225), (38, 30, 250), (197, 36, 109), (79, 244, 251), (39, 114, 147), (246, 41, 35), (144, 7, 4), (17, 2, 108), (231, 163, 197), (20, 201, 208), (111, 2, 46), (230, 127, 14), (115, 2, 1), (4, 115, 62), (234, 173, 169), (0, 117, 120), (0, 253, 240), (251, 5, 23), (0, 84, 0)]

turtle.colormode(255)

tur = t()
tur.hideturtle()
tur.setheading(220)
tur.penup()
tur.forward(290)
for j in range(10):
    tur.setheading(0)
    for _ in range(10):
        tur.pendown()
        tur.dot(20, random.choice(color_list))
        tur.penup()
        tur.forward(50)
    tur.setheading(90)
    tur.forward(50)
    tur.setheading(180)
    tur.forward(500)






screen = Screen()
screen.exitonclick()
