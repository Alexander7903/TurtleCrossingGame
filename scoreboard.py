from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(y=260, x=-220)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=FONT)




