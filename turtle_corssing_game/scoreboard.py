from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.color('black')
        self.level = 1
        # self.write(f'Level:{self.level}', align='center', font=FONT)
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        
        self.write('GAME OVER !', align='center', font=FONT)

    
    
    def update_score(self):
        self.clear()
        self.write(f'Level:{self.level}', align='center', font=FONT)

    def incerease_score(self):
        self.level = self.level +1 
        self.update_score()


