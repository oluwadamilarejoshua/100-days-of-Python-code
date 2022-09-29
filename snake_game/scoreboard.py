from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 10, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1

