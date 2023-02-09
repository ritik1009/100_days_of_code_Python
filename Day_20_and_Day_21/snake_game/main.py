from turtle import Turtle,Screen
import snake
import time
import food
import score

s1 = Screen()
s1.setup(width = 600,height =600)
s1.bgcolor('black')
s1.title('Snake game')
s1.tracer(0)
sn1 = snake.Snake()
f1 = food.Food()
score_ = score.Score()

s1.listen()
s1.onkeypress(sn1.up,'Up')
s1.onkeypress(sn1.down,'Down')
s1.onkeypress(sn1.left,'Left')
s1.onkeypress(sn1.right,'Right')
#total_turtles = []
#starting_position = [(0,0),(-20,0),(-40,0)]
#for i in starting_position:
#    t1 = Turtle('square')
#    t1.color('white')
#    t1.penup()
#    t1.goto(i)
#    total_turtles.append(t1)


game_is_on = True
while game_is_on:
    s1.update()
    time.sleep(0.1)
    sn1.move()

    # Detect 
    if sn1.head.distance(f1)<15:
        f1.refresh()
        score_.update_score()
        sn1.extend()
    
    # Detect colision with the wall
    if sn1.head.xcor()<-300 or sn1.head.xcor()>300 or sn1.head.ycor()<-300 or sn1.head.ycor()>300:
        game_is_on =False
        score_.game_over()

    # Detect colision with tail
    for i in sn1.total_turtles[1:-1]:
        if sn1.head.distance(i)<5:
            game_is_on =False
            score_.game_over()
s1.exitonclick()