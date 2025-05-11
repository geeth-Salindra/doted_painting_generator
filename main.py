# import colorgram
#
# rgb_colors=[]
# colors = colorgram.extract('images1.jpeg', 16)
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)


tim=Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(252, 241, 248), (185, 176, 5), (186, 3, 69), (5, 143, 36), (243, 22, 152), (198, 5, 2), (241, 66, 4), (43, 195, 237), (88, 2, 91), (5, 130, 207), (248, 69, 14), (234, 155, 52), (234, 12, 135)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots=100

for dot_count in range(1,num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







screen=Screen()
screen.exitonclick()