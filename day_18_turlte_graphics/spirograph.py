import turtle as t
from turtle import Screen
import random



t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    color =(r,g,b)
    return color

spyro = t.Turtle()

spyro.speed(50)

for i in range (160):
    spyro.color(random_color())
    spyro.circle(75)
    spyro.right(2)


screen = Screen()
screen.exitonclick()