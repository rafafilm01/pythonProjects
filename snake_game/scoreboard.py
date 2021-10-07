from turtle import Turtle
ALINGMENT = 'center'
FONT= ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.score = 0        
        self. color('white')
        self.penup()
        self.goto(-10, 265)
        self.hideturtle()
        self.update_score()
        
        

    def update_score(self):
        self.write(f'score: {self.score}', False, align=ALINGMENT, font=FONT)

    def increase_score(self):
        
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(-0, 0)
        self.write('GAME OVER', align=ALINGMENT, font=FONT )

        
        

