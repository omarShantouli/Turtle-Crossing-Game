from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.color("white")
        self.setpos(0, 220)
        self.write(f"{self.left_score}          {self.right_score}", align="center", font=('Arial', 50, 'normal'))
        self.hideturtle()
        self.mid_line = self.create_line()


    def create_line(self):
        x = 290
        for _ in range(0, 30):
            t = Turtle()
            t.penup()
            t.color("white")
            t.shape("square")
            t.shapesize(0.4, 0.08)
            t.setpos(0, x)
            x -= 20

    def inc(self, player):
        if player == "right":
            self.right_score += 1
        elif player == "left":
            self.left_score += 1
        self.clear()
        self.write(f"{self.left_score}          {self.right_score}", align="center", font=('Arial', 50, 'normal'))
