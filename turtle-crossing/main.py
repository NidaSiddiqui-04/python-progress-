from  turtle import Screen
import time
from player import Player
from car_manager import  CarManager
from score_board import ScoreBoard

screen=Screen()
screen.setup(600,600)
screen.tracer(0)
player=Player((0,-290))
screen.listen()
screen.onkey(fun=player.move_up,key="Up")
car=CarManager()
score=ScoreBoard()

game_on=True
while game_on:
    screen.update()
    time.sleep(player.move_speed)

    car.create_car()
    car.move_car()
    for car_q in car.all_cars:
        if car_q.distance(player)<20:
            score.game_over()
            game_on=False
    if player.ycor()==280 and player.xcor()==0:
        player.refresh()
        score.increase()

screen.exitonclick()