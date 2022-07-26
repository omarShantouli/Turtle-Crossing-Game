import random
import turtle
from turtle import Turtle, Screen
from player import Player
from random import randint
from car import Car
from time import sleep
from leve_board import  Level

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#546a7b")
turtle.tracer(0)
screen.listen()
leve_board = Level()

player = Player()
screen.onkey(player.up, "Up")

colors = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "orange", "brown", "purple"]
cars = []
game_on = True
while game_on:
    screen.update()
    x = randint(1, 4)
    if x == 1:
        car = Car()
        cars.append(car)
    for car in cars:
        car.move()
    for c in cars:
        if player.distance(c) < 30:
            game_on = False
            leve_board.game_over()
    if player.ycor() > 250:
        player.goto(0, -275)
        leve_board.inc_level()
        Car.speed += 10
    sleep(0.1)

screen.exitonclick()
