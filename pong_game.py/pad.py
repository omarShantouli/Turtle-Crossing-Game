from turtle import Turtle

class Pad(Turtle):
    def __init__(self, s):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.setheading(90)
        self.color('white')
        self.penup()
        if s == "right":
            self.setpos(350, 0)
        else:
            self.setpos(-350, 0)

    def up(self):
        if self.ycor() <= 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

