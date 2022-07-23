from turtle import Turtle, Screen
from random import choice

screen = Screen()
colors = ["yellow", "red", "green", "brown", "orange", "pink", "purple"]
x = 255
s = 100
con = []
for i in range(1, 7):
    t = Turtle()
    con.append(t)
    t.penup()
    t.shape("turtle")
    t.color(colors[i])
    t.setpos(x = -350, y = x)
    x -= s
des = [10, 20, 30, 40, 50]
over = 1
winner = ""
guess = screen.textinput("Guess", "Guess who will win")
while over:
    for c in con:
        if c.xcor() >= 320:
            winner = c.color()[0]
            over = 0
            break
        c.forward(choice(des))

if winner == guess:
    print(f"You'r right the {winner} turtle is the winner")
else:
    print(f"No, the {winner} turtle is the winner")



screen.exitonclick()