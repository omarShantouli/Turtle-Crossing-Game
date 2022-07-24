import turtle
from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=680, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

turtle.tracer(0)
snake = Snake()
food = Food()
with open("best") as file:
    h = file.read()
score = Score(int(h))

game_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
while game_on:
    if snake.head.distance(food.food) < 15:
        food.pos()
        score.inc()
        snake.eat()
    screen.update()
    x = snake.head.xcor()
    y = snake.head.ycor()
    snake.head.forward(20)
    for i in range(1, len(snake.segments)):
        xx = snake.segments[i].xcor()
        yy = snake.segments[i].ycor()
        snake.segments[i].setpos(x, y)
        x = xx
        y = yy
    sleep(0.1)
    if snake.head.xcor() > 320 or snake.head.xcor() < -340 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        game_on = False
        score.game_over()
    for s in snake.segments:
        if s != snake.head:
            if s.distance(snake.head) < 10:
                game_on = False
                score.game_over()

print(f"Your Score is {score.val}")
if score.val > int(h):
    with open("best", mode="w") as file:
        file.write(str(score.val))

screen.exitonclick()

