from turtle import Turtle
from random import randint, choice
class Car(Turtle):
    speed = 15
    def __init__(self):
        super().__init__()
        self.colors = ["blue", "green", "cyan", "magenta", "yellow", "black", "orange", "brown", "purple"]
        self.shape("square")
        self.shapesize(1.5, 3)
        self.penup()
        self.color(choice(self.colors))
        self.goto(400, randint(-230, 230))

    def move(self):
        self.goto(self.xcor() - self.speed, self.ycor())
