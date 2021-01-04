from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 320


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=0, y=new_y)
