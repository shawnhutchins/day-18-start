from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(10)
timmy.width(10)
line_length = 25

colors = ["red", "purple3", "LimeGreen", "DeepSkyBlue2", "gold1", "tan3"]
directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(directions))
    timmy.forward(line_length)

screen = Screen()
screen.exitonclick()