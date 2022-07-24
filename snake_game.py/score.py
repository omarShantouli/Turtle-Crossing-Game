from turtle import Turtle

class Score:
    def __init__(self, h):
        self.val = 0
        self.highest = h
        self.board = self.create()


    def create(self):
        self.score = Turtle()
        self.score.penup()
        self.score.color("white")
        self.score.setpos(-40, 270)
        self.score.write(f"Score: {self.val}    Highest: {self.highest}", align="center", font=('Arial', 20, 'normal'))
        self.score.hideturtle()

    def inc(self):
        self.val += 1
        self.score.clear()
        self.board = self.create()

    def game_over(self):
        self.game = Turtle()
        self.game.penup()
        self.game.setpos(0, 0)
        self.game.color("white")
        self.game.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))
