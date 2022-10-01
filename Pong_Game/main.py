from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_position = (350, 0)
l_position = (-350, 0)

r_paddle = Paddle(r_position)
l_paddle = Paddle(l_position)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    ball.ball_right_up()
    ball.fd(15)
    screen.update()
    time.sleep(1)

screen.exitonclick()
