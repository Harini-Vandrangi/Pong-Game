from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
        self.move_car()

    def create_car(self):
        self.shape("square")
        self.shapesize(1, 3)
        self.color(choice(COLORS))
        self.penup()
        self.goto(280, randint(-200, 200))

    def move_car(self):
        self.backward(STARTING_MOVE_DISTANCE)
        if self.xcor() < -300:
            self.goto(280, randint(-200, 200))

    def speed_increase(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE = MOVE_INCREMENT + STARTING_MOVE_DISTANCE
