from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(x=-280,y=250)
        self.write(arg=f"level {self.level}:",align="left",font=("Arial",20,"normal"))
    def increase(self):
        self.level+=1
        self.clear()
        self.write(arg=f"level {self.level}:", align="left", font=("Arial", 20, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",align="center",font=("Arial",20,"normal"))
