import time
from turtle import Screen
from scoreboard import GameScore
from snake import Snake
from food import Food



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")


screen.tracer(0)
snake=Snake()
food=Food()
score1=GameScore()



screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on=True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    """detect collision with food."""
    if snake.head.distance(food)<25:
        food.refresh()
        snake.extent()
        score1.increase_score()
        """detect collision with wall"""
    if snake.head.xcor() > 300 or snake.head.xcor()< -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on=False
        score1.game_over()
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment)<10:
    #         game_on=False
    #         score1.game_over()



screen.exitonclick()




















































