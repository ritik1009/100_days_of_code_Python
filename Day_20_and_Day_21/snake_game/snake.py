from turtle import Turtle
starting_position = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.total_turtles = []
        self.create_snake()
        self.head = self.total_turtles[0]

    def create_snake(self):
        for i in starting_position:
            self.add_segment(i)
            

    def add_segment(self,position):
        t1 = Turtle('square')
        t1.color('white')
        t1.penup()
        t1.goto(position)
        self.total_turtles.append(t1)

    def extend(self):
        self.add_segment(position=self.total_turtles[-1].position())

    def move(self):
        for seg_num in range(len(self.total_turtles)-1, 0, -1):
            new_x = self.total_turtles[seg_num-1].xcor()
            new_y = self.total_turtles[seg_num-1].ycor()
            self.total_turtles[seg_num].goto(new_x, new_y)
        self.total_turtles[0].forward(20)
        

    def up(self):
        if self.head.heading() !=down:
            self.head.seth(up)
    
    def right(self):
        if self.head.heading() !=left:
            self.total_turtles[0].seth(right)

    def left(self):
        if self.head.heading() != right:
            self.total_turtles[0].seth(left)

    def down(self):
        if self.head.heading() != up:
            self.total_turtles[0].seth(down)
