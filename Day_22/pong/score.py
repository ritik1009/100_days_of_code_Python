from turtle import Turtle
align = 'center'
format = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 210)
        self.write(f"Score: {self.score_left} ", align=align, font=format)
        self.goto(100, 210)
        self.write(f"Score: {self.score_right} ", align=align, font=format)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=align, font=format)

    def update_left_score(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def update_right_score(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()
