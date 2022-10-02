import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
state_data = pd.read_csv('50_states.csv')
all_states = state_data.state.to_list()
score = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f'{score}/50 states correct', prompt='What another state name?').lower()
    if answer_state in all_states:
        score += 1
        t = turtle.Turtle()
        t.pu()
        state_position = state_data[state_data == answer_state]
        t.goto(state_position.x, state_position.y)
        t.write('here')
        # print(state_data[])


screen.exitonclick()
