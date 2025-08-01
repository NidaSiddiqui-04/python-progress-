from turtle import Turtle
import random



COLORS=["red","green","blue","purple","grey","yellow"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10
class CarManager:
    def __init__(self):

        self. all_cars=[]

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==2:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-200,200)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)