from turtle import Turtle
STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.seth(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def reset_position(self):
        self.goto(STARTING_POSITION)

