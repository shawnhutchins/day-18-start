import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()

colors = [(235, 39, 116), (216, 163, 60), (141, 26, 67), (237, 70, 38), (14, 142, 90), (176, 162, 48), (177, 41, 94),
          (33, 122, 187), (54, 189, 226), (242, 219, 56), (78, 22, 71), (128, 190, 100), (198, 63, 37), (26, 169, 124),
          (248, 224, 1), (201, 137, 167)]

x = -225
y = -225
offset = 50
dot_size = 20

for _ in range(10):
    for _ in range(10):
        timmy.teleport(x, y)
        timmy.dot(dot_size, random.choice(colors))
        x += offset
    x = -225
    y += offset

screen = t.Screen()
screen.exitonclick()