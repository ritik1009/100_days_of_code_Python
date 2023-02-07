from turtle import Turtle, colormode,Screen
import random

colormode(255)
t1 = Turtle()
t1.speed(0)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t1.color(random_color())
        t1.circle(100)
        t1.setheading(t1.heading() + size_of_gap)

draw_spirograph(5)

s1 =Screen()
s1.exitonclick()