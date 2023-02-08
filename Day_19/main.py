from turtle import Turtle,Screen

t1 = Turtle()
s1 = Screen()

def move_forward():
    t1.forward(10)


def move_backward():
    t1.backward(10)


def move_left():
    t1.left(10)


def move_right():
    t1.right(10)

def clear_screen():
    t1.clear()
    t1.penup()
    t1.home()
    t1.pendown()
s1.listen()
s1.onkey(key="w",fun=move_forward)
s1.onkey(key="s",fun=move_backward)
s1.onkey(key="a",fun=move_left)
s1.onkey(key="d",fun=move_right)
s1.onkey(key="c",fun=clear_screen)
s1.exitonclick()