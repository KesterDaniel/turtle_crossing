import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.player_move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect if player reaches the other side
    if player.ycor() == player.finish_line:
        player.player_start()
        score_board.increase()
        car_manager.increase_speed()

    # detecting player collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            score_board.game_over()
            game_is_on = False


screen.exitonclick()