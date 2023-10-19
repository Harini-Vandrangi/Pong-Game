from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 230


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def move_back(self):
        self.goto(STARTING_POSITION)