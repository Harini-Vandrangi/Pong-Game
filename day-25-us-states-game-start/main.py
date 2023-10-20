from turtle import Turtle, Screen
import pandas
FONT = ("Ariel", 14, "bold")
SMALL_FONT = ("Ariel", 7, "normal")
screen = Screen()
turtle =Turtle()

score = 0
error = 0
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

states = pandas.read_csv("50_states.csv")
state_list = states.state.to_list()
print(state_list)
game_is_on = True
tim = Turtle()
tim.hideturtle()
tim.penup()

while game_is_on:
    answer = screen.textinput(f"{score}/50 States Correct", "What's another state name?").title()
    if answer in state_list:
        score += 1
        row = states[states.state == answer]
        tim.goto(int(row.x), int(row.y))
        tim.write(f"{answer}", align="center", font=SMALL_FONT)
    elif answer == "Exit":
        turtle.write("GAME OVER.", align="center", font=FONT)
        game_is_on = False
        break
    else:
        error += 1
        if error == 3 or score == 50:
            turtle.write("GAME OVER.", align="center", font=FONT)
            game_is_on = False

screen.exitonclick()
