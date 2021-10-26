from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()

def color():
    r=random.random()
    g=random.random()
    b=random.random()
    tim.color(r,g,b)


def move_forward():
    tim.forward(10)



def move_backward():
    tim.backward(10)


def rotate_left():
    tim.left(10)


def rotate_right():
    tim.right(10)

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkeypress(key="c",fun=tim.clear)
screen.onkeypress(key="x",fun=color)
screen.exitonclick()
