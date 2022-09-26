from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', "yellow", "green", "blue", "purple"]
y_coord = [-100, -60, -20, 20, 60, 100]
all_turtle = []

if user_bet:
    is_on = True

for tut_ind in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.color(colors[tut_ind])
    turt.penup()
    turt.goto(x=-230, y=y_coord[tut_ind])
    all_turtle.append(turt)


while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} is the winner")
            else:
                print(f"You lost! {winning_color} is the winner")

        movement_dist = random.randint(0, 10)
        turtle.forward(movement_dist)


screen.exitonclick()
