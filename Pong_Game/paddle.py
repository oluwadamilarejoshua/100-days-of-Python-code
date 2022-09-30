from turtle import Turtle
UP, DOWN = 90, 270


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def listen(self):
        pass

    def up(self):
        self.heading(UP)

    def down(self):
        self.heading(DOWN)
