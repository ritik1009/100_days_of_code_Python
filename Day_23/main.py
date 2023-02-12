import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)
p1 = Player()
game_is_on = True
screen.listen()
car = CarManager()
score_board = Scoreboard()
screen.onkey(p1.move_up,'Up')
screen.onkey(p1.move_down,'Down')
while game_is_on:
    time.sleep(.1)
    screen.update()
    car.create_car()
    car.move()
    for i in car.total_car:
        if i.distance(p1)<10:
            game_is_on = False
            score_board.gameover()

    if p1.ycor()>220:
        p1.reset_position()
        score_board.update_level()
        car.level_up()

screen.exitonclick()
