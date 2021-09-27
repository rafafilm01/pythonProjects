from turtle import Turtle, Screen
import random

colors =[ 'yellow', 'gold', 'orange', 'red',  'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray',]

walk_direction= [90, 180, 270, 0]

random_turtle = Turtle()
random_turtle.shape('circle')
random_turtle.width(10)
random_turtle.speed(10)

for i in range (500):
    random_turtle.forward(25)
    random_turtle.setheading(random.choice(walk_direction))
    random_turtle.color(random.choice(colors))

screen = Screen()
screen.exitonclick()