from turtle import Turtle,Screen
import turtle
import pandas as pd
screen = Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
t1 = Turtle()
t1.color('black')
t1.penup()
t1.hideturtle()
# Importing the csv

us_states_data = pd.read_csv('50_states.csv')
states_data = us_states_data.state.to_list()
x_cord = us_states_data.x.to_list()
y_cord = us_states_data.y.to_list()
game_is_on =True
screen.listen()

def gameover():
    game_is_on = False

screen.onkeypress(gameover,'q')
number_of_state_guessed = []
total_state = len(states_data)
while game_is_on:
    answer_state = screen.textinput(title=f'{len(number_of_state_guessed)}/{total_state} Guess the state',prompt='Whats another state name?').title()
    if answer_state == 'Exit':
        missing_state = []
        for states in states_data:
            if states not in number_of_state_guessed:
                missing_state.append(states)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv('states_to_learn.csv')
        game_is_on = False
    if answer_state in states_data:
        state_index = states_data.index(answer_state)
        number_of_state_guessed.append(answer_state)
        x = x_cord[state_index]
        y = y_cord[state_index]
        number_of_state_guessed +=1
        t1.goto(x,y)
        t1.write(answer_state,align='center')