FONT = ("Courier", 24, "normal")
align = 'Center'
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-150, 210)
        self.write(f"Level: {self.score} ", align=align, font=format)

    def update_level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write('Game Over', align=align, font=format)
