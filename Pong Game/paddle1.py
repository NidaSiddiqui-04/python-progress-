from turtle import Turtle

UP=90
DOWN=270

class Paddle(Turtle):
         def __init__(self,start_pos):
             super().__init__()

             self.shape("square")
             self.color("white")
             self.penup()
             self.turtlesize(stretch_wid=5,stretch_len=1,outline=1)
             self.setposition(start_pos)

         def move_up(self):
             new_y = self.ycor() + 20
             self.goto(self.xcor(), new_y)

         def move_down(self):
             new_y = self.ycor() - 20
             self.goto(self.xcor(), new_y)