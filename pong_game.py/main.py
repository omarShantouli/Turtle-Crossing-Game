import turtle
from pad import Pad
from score_board import Score_board
from ball import Ball
from time import sleep

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
turtle.tracer(0)

right_pad = Pad("right")
left_pad = Pad("left")
score_board = Score_board()
ball = Ball()

screen.listen()
screen.onkey(right_pad.up, "Up")
screen.onkey(right_pad.down, "Down")
screen.onkey(left_pad.up, 'w')
screen.onkey(left_pad.down, 's')

game_on = True
while game_on:

    ball.move()

    if ball.xcor() > 390:
        ball.setpos(0, 0)
        score_board.inc("left")
    elif ball.xcor() < -390:
        ball.setpos(0, 0)
        score_board.inc("right")

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    sleep(0.02)
    screen.update()


screen.exitonclick()

