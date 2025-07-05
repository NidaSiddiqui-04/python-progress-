from turtle import Turtle
import random





class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5)
        self.penup()
        self.color("blue1")
        self.speed(0)
        rand_x=random.randint(-280,280)
        rand_y=random.randint(-280,280)
        self.goto(rand_x,rand_y)

    def refresh(self):
        self.shape("circle")
        self.shapesize(.5)
        self.penup()
        self.color("blue1")
        self.speed(0)
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
