from turtle import Turtle

class GameScore(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score :{self.score}",align="center",font=("Arial",20,"normal"))
    def game_over(self) -> None:

        self.color("white")
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER ", align="center", font=("Arial", 20, "normal"))



    def increase_score(self) -> None:
        self.score+=1
        self.clear()


        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
