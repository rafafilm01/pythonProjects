from main import turn_left
from turtle import Turtle , Screen
import random

screen= Screen()
screen.setup(width=500, height=400)
is_race_on = False

# ask for user input to bet on a turtle
user_bet = screen.textinput(title='make your bet', prompt='Which turtle will win the race  ? ' )
colors= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles =[]

y= -100
for turtle_index in range (6):
    
    race_turtle =Turtle(shape='turtle')
    race_turtle.penup()
    race_turtle.color(colors[turtle_index])
    race_turtle.goto(-230, y)
    y += 35
    all_turtles.append(race_turtle)

 
if user_bet:
    is_race_on = True

while is_race_on :

    for turtle in all_turtles:
        # if turtle.xcor() > 230:
        #     is_race_on = False
        #     winning_colour = turtle.pencolor()
        #     if winning_colour == user_bet:
        #         print('Your turtle has won ! ')
        #     else:
        #         print('You have lost ! ')

                     
        random_distance  = random.randint(0,10)
        turtle.forward(random_distance)
        

screen.exitonclick()

