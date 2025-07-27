from turtle import Turtle, Screen
import random

timmy = Turtle()
#figure out how to control turtle speed
timmy.speed(10)
screen = Screen()

#make a list of colors to chose from
colors = ["red", "purple3", "LimeGreen", "DeepSkyBlue2", "gold1", "tan3"]
#make a variable to control line width
line_width = 10
#make a variable to control line length
line_length = 50
#make a variable to control line color
line_color = random.choice(colors)
#make a variable to control number or iterations
iterations = 30

#make a function to randomly pick an int from -1 to 1
#make variables for x and y axis
#randomly pick x or y axis
    #randomly pick 1 or -1
#make the loop to paint the lines for number of iterations

screen.exitonclick()