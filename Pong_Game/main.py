from turtle import Screen, Turtle
# from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")



screen.exitonclick()
