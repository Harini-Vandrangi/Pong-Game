from turtle import Turtle
LEFT = (-490, 0)
RIGHT = (480, 0)

class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__("square")
        self.color("white")
        self.turtlesize(3, 1)  # stretching the turtle to become a paddle
        self.penup()
        if direction == "left":
            self.goto(LEFT)
        else:
            self.goto(RIGHT)

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        if y < 230:
            self.goto(x, y)


    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        if y > -230:
            self.goto(x, y)



