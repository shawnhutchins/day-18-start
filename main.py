from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

screen = Screen()
screen.colormode(255)

sides = 3
max_sides = 10
side_len = 100

def new_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    new_color = [r, g, b]
    return new_color

line_color = new_random_color()

while sides != max_sides:
    timmy.color((line_color[0], line_color[1], line_color[2]))
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)
    sides += 1
    line_color = new_random_color()

screen.exitonclick()