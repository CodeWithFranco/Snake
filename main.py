import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)  # size of the screen
screen.bgcolor("black")  # screen background color
screen.title("My Snake Game")


"""
Use For-Loop to get access to the Tuple list values while creating a new object for Turtle
"""
start_positions = [(0, 0), (-20, 0), (-40, 0)]  # Tuple list
for position in start_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


screen.exitonclick()