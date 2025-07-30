import turtle as t
import colorgram
import pprint

t.colormode(255)
timmy = t.Turtle()

colors = colorgram.extract("image.jpg", 20)
t_colors = []
pprint.pp(colors[0].rgb.r)
for index in range(len(colors)):
    colors[index].rgb.r

screen = t.Screen()
screen.exitonclick()