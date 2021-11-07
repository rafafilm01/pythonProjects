from turtle import Turtle

PADDLE_SPEED =25

class Paddlle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.goto(position,0)
        self.setheading(90)
        self.shapesize(1, 5)
        self.color('white')
        


    def move_up(self):
        self.forward(PADDLE_SPEED)

    def move_down(self):
        self.bk(PADDLE_SPEED)
