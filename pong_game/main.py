from turtle import Turtle, Screen, left
from paddle import Paddlle
from ball import Ball
from scoreboard import Scoreboard
import time


game_is_on = True
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)




left_paddle= Paddlle(-350)
right_paddle=Paddlle(350)
ball = Ball()
scoreboard = Scoreboard()



# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
    
#     ball.move()



screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down,'Down')
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')



while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    ball.move()

    #detecing wall bounce
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.wall_bounce()

    #detecting collision with r_paddle
    if ball.distance(right_paddle) <50 and ball.xcor() > 320 or ball.distance(left_paddle) <50 and ball.xcor() < -320:
        ball.paddle_bounce()

#seperate conditions for left and right paddle to make it easier to keep score (later) 
    if ball.xcor() > 400:  
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.r_point()


screen.exitonclick()