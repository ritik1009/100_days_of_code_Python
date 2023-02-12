from turtle import Turtle
import random
y_cord = [0,30,60,90,120,-30,-60,-90,-120,-150]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import time


class CarManager:
    def __init__(self):
        self.total_car = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            t1 = Turtle()
            t1.shape('square')
            t1.shapesize(stretch_wid=1,stretch_len=2)
            t1.color(random.choice(COLORS))
            t1.penup()
            y_cord = random.randint(-180, 180)
            t1.goto(250, y_cord)
            t1.seth(180)
            t1.speed(1)
            self.total_car.append(t1)
        
    def move(self):
        for i in self.total_car:
            i.forward(self.car_speed)

    def level_up(self):
        self.car_speed +=MOVE_INCREMENT
