import turtle as t
import random

timmy = t.Turtle()
timmy.speed(0)

t.colormode(255)

def new_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(new_random_color())
        timmy.circle(100)
        timmy.right(size_of_gap)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()