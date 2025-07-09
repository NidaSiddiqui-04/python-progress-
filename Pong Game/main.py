"""creating a screen"""
import time
from turtle import Screen
from ball import Ball

from paddle1 import Paddle
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(height=600,width=800)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
""" creating a paddle"""
paddle_1=Paddle((350,0))
paddle_2=Paddle((-350,0))
ball=Ball((0,0))
score=ScoreBoard()




screen.listen()
screen.onkey(paddle_1.move_up,key="Up")
screen.onkey(paddle_1.move_down,key="Down")
screen.onkey(paddle_2.move_up,key="w")
screen.onkey(paddle_2.move_down,key="s")
game_on=True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # Right paddle collision
    if ball.distance(paddle_1)<50 and ball.xcor()>330 or  ball.distance(paddle_2)<50 and ball.xcor()<-330:
        ball.bounce_x()

    if ball.xcor()>360  :
        ball.reset_pos()
        ball.move_speed=.1
        ball.bounce_x()

        score.l_point()
    if ball.xcor()<-360:
        ball.reset_pos()
        ball.move_speed=.1
        ball.bounce_x()
        score.r_point()
screen.exitonclick()