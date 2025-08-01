from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0
STARTING_POSITION=[(-20,0),(0,0),(20,0)]
class Snake:
    def __init__(self):

       self.segments=[]
       self.speed="fast"
       self.create_snake()
       self.head=self.segments[0]
       # self.head=self.segment[0]
    def create_snake(self):
       for snake in STARTING_POSITION:
            self.add_segment(snake)
    def add_segment(self,snake):
        seg1 = Turtle("square")
        seg1.color("white")
        seg1.penup()
        seg1.goto(snake)
        self.segments.append(seg1)
    def extent(self):
        self.add_segment(self.segments[-1].position())



    def move(self):

            for seg_num in range(len(self.segments) - 1, 0, -1):

                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.head.fd(20)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:

             self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
             self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)