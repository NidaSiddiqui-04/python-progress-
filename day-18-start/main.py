import random  # from turtle import *
#
# timmy=Turtle()
# timmy.shape("turtle")
#
# timmy.color("cyan1")
# for i in range(1,5):
#     timmy.forward(100)
#
#     timmy.right(90)

import turtle as t # aliasing modules
from random import choice,randint
import randomwalk



timm=t.Turtle()
timm.shape("turtle")

# for i in range(15):
#     timm.pendown()
#     timm.forward(10)
#     timm.penup()
#     timm.forward(10)
"""360/5=72 i.e.angle of  pentagon is 72 degree
 ,similarly 360/8 =45 i.e. angle of octagon is 45 degree"""
# color=["red","green","blue","brown","yellow","coral1","blue1"]
# for sides in range(3,11):
#     timm.color(choice(color))
#     def shapes(num_sides):
#         angle=360/num_sides
#         for i in range(num_sides):
#             timm.forward(100)
#             timm.right(angle)
#     shapes(side

# direction=[0,90,180,270]
# for i in range (200):
#      timm.pensize(5)
#      timm.speed(0)
#      timm.forward(20)
#      timm.right(choice(direction))
#      timm.color(choice(color))
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r,g,b)
    return color
#
# direction=[0,90,180,270]
# for i in range (200):
#      timm.pensize(5)
#      timm.speed(0)
#      timm.forward(20)
#      timm.left(choice(direction))
#      timm.color( random_color())


timm.speed(0)
for i in range(200):
    timm.color(random_color())
    timm.circle(100 )
    timm.backward(0.1)
    timm.left(3)









screen=t.Screen()
screen.exitonclick()