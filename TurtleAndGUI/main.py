from turtle import Turtle, Screen

tim = Turtle()
times = 0

while times < 4:
    times += 1
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()
