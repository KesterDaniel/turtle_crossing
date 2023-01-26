import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.player_move)

game_is_on = True

cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    car.forward(car.move_distance)
    cars.append(car)
    for car in cars:
        car.forward(car.move_distance)

    # detect if player reaches the other side
    if player.ycor() == player.finish_line:
        player.player_start()

    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
