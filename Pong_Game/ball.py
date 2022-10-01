from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("white")

    def ball_right_up(self):
        new_x, new_y = self.xcor() + 10, self.ycor() + 10
        self.goto(new_x, new_y)
