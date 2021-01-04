import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = []

for x in range(30):
    new_car = CarManager()
    cars.append(new_car)

player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars[:10]:
        car.move()
        if car.xcor() < -320:
            car.go_back()
        if player.distance(car) < 20:
            player.goto(0, -280)
            scoreboard.game_over()
            game_is_on = False
    if time.process_time() > 0.6:
        for car in cars[10:20]:
            car.move()
            if car.xcor() < -320:
                car.go_back()
            if player.distance(car) < 20:
                player.goto(0, -280)
                scoreboard.game_over()
                game_is_on = False
    if time.process_time() > 1.2:
        for car in cars[20:30]:
            car.move()
            if car.xcor() < -320:
                car.go_back()
            if player.distance(car) < 20:
                player.goto(0, -280)
                scoreboard.game_over()
                game_is_on = False

    if player.ycor() > 290:
        for car in cars:
            car.speedup()
        player.goto(0, -280)
        scoreboard.level_up()
        scoreboard.clear()
        scoreboard.update_scoreboard()














screen.exitonclick()