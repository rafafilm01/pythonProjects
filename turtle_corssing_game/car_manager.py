from turtle import Turtle
import random
from typing import Collection

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars =[]
        self.car_speed= STARTING_MOVE_DISTANCE


    def create_car(self):
        #dice roll - random chance generator, every time the screen refreshes (screen.timeout(0.1)) a new random check is being carried out , only when it falls to 1 a new car will be generated 
        random_chance = random.randint(1,6)
        if random_chance ==1 :
            
            new_car=Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            
            new_car.color(random.choice(COLORS))
            random_y =random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)



    def move_cars(self):
        for car in self.all_cars:
            car.back(self.car_speed)

#speeding up the cars when u level up
    def increase_speed(self):
        self.car_speed +=MOVE_INCREMENT
        



