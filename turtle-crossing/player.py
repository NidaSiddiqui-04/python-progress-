from turtle import Turtle


class Player(Turtle):
    def __init__(self,start_pos,):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(start_pos)
        self.move_speed=.1



    def move_up(self):
        new_y=self.ycor()+10
        # self.right(0)
        self.goto(self.xcor(),new_y)
    def refresh(self):
        self.goto(0,-280)
        self.move_speed*=.9