from turtle import Turtle, colormode
import random


t1 = Turtle()

colormode(255)

#colors = ['red','black','green','yellow','blue','skyblue','purple','orange']

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

sides_ = [0,90,180,270]
t1.pensize(6)
t1.speed(0)
for i in range(200):
    t1.color(random_color())
    t1.forward(30)
    sides = random.choice(sides_)
    t1.seth(sides)