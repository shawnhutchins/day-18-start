import turtle as t
import random

timmy = t.Turtle()
timmy.speed(10)
timmy.width(10)
line_length = 25

t.colormode(255)

directions = [0, 90, 180, 270]

def new_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(200):
    timmy.color(new_random_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(line_length)

screen = t.Screen()
screen.exitonclick()