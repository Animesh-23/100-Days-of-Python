from turtle import Turtle, Screen, resetscreen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def counter_clockwise():
    angle = timmy.heading() + 5
    timmy.setheading(angle)


def clockwise():
    angle = timmy.heading() - 5
    timmy.setheading(angle)


def clear_screen():
    resetscreen()


screen.listen()

screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=counter_clockwise)
screen.onkeypress(key='d', fun=clockwise)
screen.onkeypress(key='c', fun=clear_screen)

screen.exitonclick()
