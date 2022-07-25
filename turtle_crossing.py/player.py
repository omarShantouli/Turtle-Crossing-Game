from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -275)
        self.setheading(90)

    def up(self):
        self.forward(20)
