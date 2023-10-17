from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=1000, height=500)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
player1 = 0
player2 = 0
name = screen.textinput("Pong Game", "Enter your names separated by space.")
names = name.split(" ")
print(names)

l_paddle = Paddle("left")
r_paddle = Paddle("right")
l_score = ScoreBoard(names[0], -100, 200)
r_score = ScoreBoard(names[1], 100, 200)
ball = Ball()

screen.listen()  # to listen to the keys


screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=r_paddle.up, key="i")
screen.onkey(fun=r_paddle.down, key="j")

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move_ball()
    # detect collision with wall
    if ball.ycor() >= 250 or ball.ycor() <= -250:  # collision with wall
        ball.bounce()
    # detect collision with paddle
    if r_paddle.distance(ball) < 25 or l_paddle.distance(ball) < 25:
        ball.bounce_back()
    if ball.xcor() > 500:
        ball.reset()  # out of bounds on right
        player1 = l_score.scoreValue(names[0])

    if ball.xcor() < -500:
        ball.reset()  # out of bounds on left
        player2 = r_score.scoreValue(names[1])

    if player1 == 5 or player2 == 5:
        l_score.gameOver()
        if player1 > player2:
            screen.textinput("Left side won the game", "Ending the game.")
        else:
            screen.textinput("Left side won the game", "Ending the game.")
        game_on = False

screen.exitonclick()
