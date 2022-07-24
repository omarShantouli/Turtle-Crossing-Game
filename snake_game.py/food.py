from turtle import Turtle
from random import randint
class Food:
    def __init__(self):
        self.food = self.create()
        self.pos()
    def create(self):
        food = Turtle()
        food.shape("circle")
        food.color("blue")
        food.shapesize(0.5)
        food.penup()
        return food

    def pos(self):
        self.food.setpos(randint(-330, 310), randint(-285, 290))
