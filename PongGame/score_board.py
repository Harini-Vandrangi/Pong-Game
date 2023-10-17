from turtle import Turtle
FONT = ("Ariel", 14, "normal")
class ScoreBoard(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"{name}: {self.score}", align="center", font=FONT)

    def scoreValue(self, name):
        self.clear()
        self.score += 1
        self.write(f"{name}: {self.score}", align="center", font=FONT)
        return self.score

    def gameOver(self):
        self.write("Game Over.", align="center", font=FONT)
