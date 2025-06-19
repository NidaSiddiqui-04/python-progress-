import random
from turtle import *




# def add(n1,n2):
#     return n1+n2
# def multi(n1,n2):
#     return n1*n2
# def calculator(n1,n2,func):
#     return func(n1,n2)
#
# """here calculator is the higher order
# function as it is taking another function as an input"""
#
# print(calculator(3,4,add))
screen=Screen()
screen.setup(width=500,height=400)

color_list=["red","green","yellow","purple","orange","brown"]
postion=[100,-100,50,-50,0,-150]
all_turtle=[]
for turtle_index in range(0,6):
    ruba=Turtle(shape="turtle")
    ruba.color(color_list[turtle_index])
    ruba.penup()
    ruba.goto(x=-240,y=postion[turtle_index])
    all_turtle.append(ruba)

bet=screen.textinput(title="make your bet",prompt="Which turtle will win the race? Enter the color: ")
if bet:
    race_on =True
while race_on:
    for turtle in all_turtle:
        if turtle.xcor()>240:
            race_on=False
            winner=turtle.pencolor()
            if winner==bet:
                print(f"you've won ,{winner} turtle is the winner")
            else:
                print(f"you've lost, {winner} turtle is the winner")


        walk=random.randint(1,10)
        turtle.forward(walk)


# screen.listen()
# angle=0
# def move_fd():
#     return ruba.forward(10)
# def move_bk():
#     return ruba.backward(10)
# def counter_clockwise():
#
#     return ruba.left(angle+10)
# def clockwise():
#     return ruba.right(angle+10)
# def circle():
#     return ruba.circle(100,20)
# def clear():
#     ruba.reset()
# screen.onkey(clear,"c")
# screen.onkey(circle,"Up")
# screen.onkey(counter_clockwise,"a")
# screen.onkey(clockwise,"d")
# screen.onkey(key="w",fun=move_fd)
# screen.onkey(key="s",fun=move_bk)
screen.exitonclick()