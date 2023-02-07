#import colorgram
#
#colors = colorgram.extract(r'D:\projects\Udemy\100-days-of-code-Python\Day_18\hirst_painting\hirst.jpg', 30)
#rgb_color = []
#for i in colors:
#    r = i.rgb.r
#    g = i.rgb.g
#    b = i.rgb.b
#    rgb_color.append((r,g,b))

#print(rgb_color)
from turtle import Turtle,Screen,colormode
import random
colormode(255)
t1 = Turtle()

colors_ =[(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)]
t1.speed(0)
t1.setheading(225)
t1.penup()
t1.hideturtle()
t1.forward(350)
t1.setheading(0)
def hirst_(number_of_dots):
    for i in range(1, number_of_dots+1):
        t1.dot(20, random.choice(colors_))
        t1.forward(50)
        if i %10 ==0:
            t1.setheading(90)
            t1.forward(50)
            t1.setheading(180)
            t1.forward(500)
            t1.setheading(0)

hirst_(100)

s1 =Screen()
s1.exitonclick()






