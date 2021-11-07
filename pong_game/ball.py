from turtle import Turtle 
import random

HEADING = [45, 135, 225, 315 ] # to use with random_start
RANDOM_DIRECTION = [-10, 10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(1,1)
        self.goto(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed =0.1
       # self.random_start()

    def move(self):
        new_x = self.xcor()  +self.x_move
        new_y = self.ycor()  +self.y_move 
        self.goto(new_x, new_y)
        #self.forward(10) to work with self.random_start , def selectes the direction and forwardpushes the ball

    def random_start (self): # alternative to randomdirection when starting the game
        self.setheading(random.choice(HEADING))

    def wall_bounce(self):
        self.y_move = self.y_move *-1
    
    def paddle_bounce(self):
        self.x_move =self.x_move *-1
        #increase the speed of ball move with each successful paddle bounce
        self.move_speed *=0.9

    def ball_reset(self):
        self.paddle_bounce()
        #reset the speed of the ball back to default 
        self.move_speed =0.1
        self.setpos(0,0)
        
        