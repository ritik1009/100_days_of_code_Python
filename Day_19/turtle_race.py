from turtle import Turtle,Screen
import random

is_race_on = False
s1 =Screen()
s1.setup(width=500,height=400)
user_bet = s1.textinput(title="Make your bet",prompt="Which Turtle will win the race? Enter a color: ")
colors = ['red','orange','green','blue','black','purple']
position = [-100,-50,0,50,100,150]

total_turtle = []
for i in range(6):
    t1 = Turtle(shape='turtle')
    t1.color(colors[i])
    t1.penup()
    t1.goto(x=-230,y=position[i])
    total_turtle.append(t1)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in total_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        random_speed = random.randint(0,10)
        turtle.forward(random_speed)

s1.exitonclick()