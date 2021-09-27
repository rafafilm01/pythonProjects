from turtle import Turtle, Screen
import heroes


def make_square(clr):
    timmothy.pendown()
    timmothy.color(clr)
    timmothy.forward(100)
    timmothy.right(90)
    timmothy.forward(100)
    timmothy.right(90)
    timmothy.forward(100)
    timmothy.right(90)
    timmothy.forward(100)

def reposition():
    timmothy.penup()
    timmothy.forward(100)
    timmothy.pendown()

timmothy =Turtle()
timmothy.shape('turtle')
timmothy.color('DarkViolet')
make_square('blue')
reposition()
make_square('red')
reposition()
make_square('black')
reposition()
make_square('green')

timmothy.penup()
timmothy.forward(50)
timmothy.right(90)
timmothy.forward(50)
for i in range(4):
    make_square('orange')
    reposition()

print(heroes.gen())
screen=Screen()
screen.exitonclick() 

