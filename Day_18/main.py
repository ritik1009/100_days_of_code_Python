from turtle import Turtle,Screen

t1 = Turtle()
t1.shape('turtle')
t1.color("Green")
t1.speed(1)
for i in range(10):
    t1.pendown()
    t1.forward(10)
    t1.penup()
    t1.forward(10)
t1.right(20)
s1 = Screen()
s1.exitonclick()