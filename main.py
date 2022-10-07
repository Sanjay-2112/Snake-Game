from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring="snake game")
screen.bgcolor("black")
screen.tracer(0)

score_card = Scoreboard()
snack = Snake()
food = Food()


screen.listen()
screen.onkey(key="Up", fun=snack.up)
screen.onkey(key="Down", fun=snack.down)
screen.onkey(key="Right", fun=snack.right)
screen.onkey(key="Left", fun=snack.left)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snack.move()

    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend_snake()
        score_card.increase_score()

    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        score_card.reset()
        snack.reset()

    for s in snack.snake_body[1:]:
        if snack.head.distance(s) < 10:
            score_card.reset()
            snack.reset()

screen.exitonclick()
