from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen 
import time


#screen set up
screen = Screen()
screen.setup(height=600 , width= 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #used to switch off the turtle animatioon , connected to .update / time.sleep
#screen set up


snake = Snake()
food = Food() #soon as food class is called everything in the def __init gets activated
scoreboard = Scoreboard()

#create control  for the snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
#create control for the snake 

 #game loop 
game_is_on = True
while game_is_on:
    screen.update() # refreshes and re-draws the screen , works in conjunction with tracer 
    time.sleep(0.1) #used for dealying the update and working the animation 
# time - refersh info. While the game is on the screen will update every 0.1 second during which the snake will move forward  
    snake.move()
    
    #detecting colision with the food (nom nom)
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect colision with the wall , if thea happens - game over 
    if  snake.head.xcor() >285 or snake.head.xcor() < -285 or snake.head.ycor() >285 or snake.head.ycor() <-285:
        scoreboard.game_over()   
        game_is_on =False     
 
    #detect collison with the body , if the head collibes with any segment in the tail
    for segment in snake.segments[1:]:
        if  snake.head.distance(segment) <10:
    # if the distance of the head is smaller than 10 to any other segments (we are looping over)
            scoreboard.game_over()
            game_is_on = False


     

screen.exitonclick()