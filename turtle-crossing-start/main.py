import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=500)
screen.title("Crossing Game")
cars = []
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.move_player, key="Up")

car = CarManager()

score = Scoreboard()
game_is_on = True
i = 0
no_cars = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i % 7 == 0 and no_cars < 10:
        car = CarManager()
        cars.append(car)
        no_cars += 1
    # print(cars)
    for car in cars:
        car.move_car()
        if car.distance(player) < 30:
            score.game_over()
            screen.textinput("GAME OVER", "Type OK to exit.")
            game_is_on = False

    if player.ycor() > 230:
        player.move_back()
        score.level_increase()
        car.speed_increase()
    i += 1
