import turtle as t
import colorgram
import pprint

t.colormode(255)
timmy = t.Turtle()

colors = colorgram.extract("image.jpg", 20)
t_colors = []

for index in range(len(colors)):
    r = colors[index].rgb.r
    g = colors[index].rgb.g
    b = colors[index].rgb.b
    t_colors.append((r, g, b))

screen = t.Screen()
screen.exitonclick()