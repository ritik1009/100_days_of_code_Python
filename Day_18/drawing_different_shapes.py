from turtle import Turtle
import random
t1 = Turtle()

colors = ['red','black','green','yellow','blue','skyblue','purple','orange']

def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        t1.forward(100)
        t1.right(angle)


for i in range(3,10):
    t1.color(random.choice(colors))
    draw_shape(i)