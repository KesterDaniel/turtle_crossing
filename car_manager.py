import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=0.8)
        self.color(random.choice(COLORS))
        self.goto(340, random.randint(-250, 250))
        self.setheading(180)
        self.move_distance = STARTING_MOVE_DISTANCE
