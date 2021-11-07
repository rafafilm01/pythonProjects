import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

#detect successful crossing    
    if player.ycor() > 280:
        player.reset_postion()
        scoreboard.incerease_score()
        car_manager.increase_speed()
#detect collisions with the cars 
    for car in car_manager.all_cars:

        if car.distance(player) < 22:
            game_is_on =False
            scoreboard.game_over()
            

screen.exitonclick()