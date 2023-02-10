from turtle import Turtle, Screen
import paddle
import ball
import time
import score



t1 = Turtle()
s1 = Screen()
s1.setup(width=700,height=500)
s1.bgcolor('black')
s1.title('Pong')
s1.tracer(0)
t1.color('white')
t1.seth(270)
t1.penup()
t1.goto(0,240)
t1.hideturtle()
p1 = paddle.Paddle(x_cor =330)
p2 = paddle.Paddle(x_cor=-330)
score_ = score.Score()
ball_ = ball.Ball()

while t1.ycor() > -240:
    t1.pendown()
    t1.forward(20)
    t1.penup()
    t1.forward(20)



s1.listen()
s1.onkey(p1.up,"Up")
s1.onkey(p1.down,"Down")
s1.onkey(p2.up,'w')
s1.onkey(p2.down,'s')

game_is_on = True
bounce = False
while game_is_on:
    s1.update()
    time.sleep(ball_.ball_speed)
    ball_.move()
    # detect collision with wall
    if ball_.ycor() > 200 or ball_.ycor() < -200 :
        ball_.bounce_y()

    # detect collision with r_paddle
    if ball_.distance(p1) < 50 and ball_.xcor() > 305 or ball_.distance(p2) < 50 and ball_.xcor() < -305:
        ball_.bounce_x()
        sleep -=.005
        #score.update_score()
    elif ball_.xcor()>320:
        #score.game_over()
        time.sleep(.5)
        ball_.reset()
        score_.update_left_score()
        sleep = .1
        #game_is_on =False
    elif ball_.xcor() < -320:
        #score.game_over()
        time.sleep(.5)
        ball_.reset()
        score_.update_right_score()
        sleep =.1
        


s1.exitonclick()