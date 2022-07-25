from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.lev = 1
        self.penup()
        self.goto(0, 260)
        self.write(f"Level {self.lev}", align= "center", font=('Arial', 24, 'normal'))
        self.hideturtle()

    def inc_level(self):
        self.clear()
        self.lev += 1
        self.write(f"Level {self.lev}", align="center", font=('Arial', 24, 'normal'))

    def game_over(self):
        t = Turtle()
        t.penup()
        t.color("red")
        t.write(f"         GAME OVER\n"+f"YOUR FINAL LEVEL IS {self.lev}", align="center", font=('Arial', 24, 'bold'))
        t.hideturtle()
