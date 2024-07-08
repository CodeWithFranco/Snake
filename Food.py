from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # inherit from turtle class
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # reduce the shape of turtle to 1/2
        self.speed("fastest")
        self.color("yellow")
        self.refresh()  # method to relocate food

    def refresh(self):
        random_x = random.randint(-280, 280)  # area is 600 x 600 (-300, 300) - lessen it a bit for visual
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)