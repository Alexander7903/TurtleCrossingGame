from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.new_y = random.randint(-280, 280)
        self.movement = 0
        self.new_x = 0
        self.new_cars()

    def move(self):
        self.movement = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(y=self.new_y, x=self.movement)

    def new_cars(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        color = random.choice(COLORS)
        self.color(color)
        self.new_x = random.randint(300, 600)
        self.new_y = random.randint(-260, 280)
        self.goto(x=self.new_x, y=self.new_y)

    def go_back(self):
        self.new_x = random.randint(300, 600)
        self.new_y = random.randint(-260, 280)
        self.goto(y=self.new_y, x=self.new_x)

    def speedup(self):
        self.movement = self.xcor() - MOVE_INCREMENT
        print(self.movement)
        self.goto(y=self.new_y, x=self.movement)





