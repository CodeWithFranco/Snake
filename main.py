"""
Date: 3/27/2024
Author: Franco Nepomuceno
Title: Snake
"""
import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # updates screen animation to 0: OFF (Fast)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Key Binding
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()  # updates the screen when snake moves
    time.sleep(0.125)  # delay for 0.125s
    snake.move()

    # Detecting food with snake
    if snake.head.distance(food) < 15:  # food is 10 x 10 pixels
        scoreboard.increase_score()
        scoreboard.update_score()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_end()  # Writes Game Over after hitting the wall
        game_is_on = False



screen.exitonclick()
