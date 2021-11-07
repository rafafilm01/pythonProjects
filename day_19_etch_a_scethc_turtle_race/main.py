from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
def move_forward():
    tim.forward(30)

def turn_left():
    tim.left(15)  

def turn_roight():
    tim.right(15)

def move_backwards():
    tim.forward(-30)

def clear_screen():
    tim.reset()

def pen_up():
    tim.penup()
    tim.color('green')

def pen_down():
    tim.pendown()
    tim.color('black')

#listeners for user input
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(turn_left, 'a')
screen.onkey(turn_roight, 'd')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=clear_screen, key='c')
screen.onkey(fun=pen_down, key='q')
screen.onkey(fun=pen_up, key='e')

screen.exitonclick()