import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=600, height=600)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'purple']
pos = [-220, -140, -60, 20, 100, 180, 260]
turtles = []

for i in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=pos[i])
    turtles.append(new_turtle)

user_guess = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? Choose a color: ")

if user_guess:
    is_race_on = True

while is_race_on:
    turtle_index = random.randint(0, 6)
    distance = random.randint(1, 10)
    turtles[turtle_index].forward(distance)
    if turtles[turtle_index].pos()[0] >= 300:
        is_race_on = False
        if turtles[turtle_index].color()[0] == user_guess:
            print("You won the bet")
        else:
            print(f"Sorry you lose {turtles[turtle_index].color()[0]} won the race")
screen.exitonclick()
