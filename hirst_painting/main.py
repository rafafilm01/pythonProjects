# extracting colours from an image 
# import colorgram

# extracting colours from an image (RGB scale) and transforming it to a tuple for re-use - use colorgram lib    

# colors = colorgram.extract('hirst.jpeg', 30)

# rgb_colors =[]
# for color in colors:
#     r =color.rgb.r
#     g =color.rgb.g
#     b= color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# extracting colours from an image (RGB scale) and transforming it to a tuple for re-use

colour_list = [(198, 12, 35), (220, 160, 68), (43, 80, 176), (237, 229, 5), (238, 40, 138), (38, 215, 72), (32, 41, 153), (205, 73, 22), (21, 149, 23), (204, 33, 101), (74, 10, 29), (181, 17, 10), (217, 140, 193), (216, 161, 9), (56, 15, 11), (18, 16, 45), (78, 211, 159), (67, 72, 222), (14, 95, 62), (80, 191, 223), (237, 159, 217), (94, 233, 197), (220, 84, 49), (5, 232, 240), (14, 65, 44)]

#obj 10 rows & 10 columns , random dots 

from turtle import Turtle, Screen
import random
import turtle

#enable colormode in turtle to allow usage of rgb
turtle.colormode(255)
#enable colormode in turtle to allow usage of rgb

hirst = Turtle()
hirst.penup()
screen= Screen()
# screen.screensize(canvwidth=100, canvheight=500)
hirst.color('white')
#start position

x = -300
y= -300
hirst.speed('fastest')
hirst.hideturtle()
hirst.setx(x)
hirst.sety(y)
hirst.color('black')

#movement
def print_1_row():
    up_1_row = 0
    for i in range (10):
        #create random color ??
        
        hirst.dot(30, random.choice(colour_list))
        hirst.forward(65)
        
    
for i in range (10):
    print_1_row()
    hirst.setx(x)
    y =y +50
    hirst.sety(y)

screen.exitonclick()


