import turtle
from turtle import Turtle as t, Screen
import random

angle = [0, 90, 180, 270]
tur = t()
turtle.colormode(255)
tur.pensize(10)
tur.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turp = (r, g, b)
    return turp


for j in range(500):
    tur.pencolor(random_color())
    tur.forward(30)
    tur.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()
