from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_seg()
        self.set_pos()
        self.head = self.segments[0]


    def create_seg(self):
        for _ in range(0, 3):
            temp = Turtle()
            temp.shape("square")
            temp.color("white")
            temp.shapesize(1, 1)
            temp.penup()
            self.segments.append(temp)
    def set_pos(self):
        self.pos = [(0, 0), (-20, 0), (-40, 0)]
        self.x = 0
        for s in self.segments:
            s.setpos(self.pos[self.x][0], self.pos[self.x][1])
            self.x += 1
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def eat(self):
        temp = Turtle()
        temp.shape("square")
        temp.color("white")
        temp.shapesize(1, 1)
        temp.penup()
        temp.setpos(self.head.position())
        self.segments.append(temp)
        self.head = self.segments[0]

