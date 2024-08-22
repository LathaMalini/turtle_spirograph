import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


def colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colours = (r, g, b)
    return random_colours


def graph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.speed("fastest")
        tim.color(colours())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


graph(5)

screen = Screen()
screen.exitonclick()
