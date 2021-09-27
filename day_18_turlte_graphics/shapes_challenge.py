from turtle import Turtle, Screen
import random

colors =[ 'yellow', 'gold',' range', 'red,' 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
sharpie = Turtle()
sharpie.shape('turtle')


def create_shapes(int):
    for i in range (int):
        sharpie.forward(100)
        sharpie.right(360/ int)
    sharpie.color(random.choice(colors))
    

value =3
for i in range (10):
    create_shapes(value)
    value += 1

screen = Screen()
screen.exitonclick()