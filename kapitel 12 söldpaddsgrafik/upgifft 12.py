# Gör en funktion kvadrat(sida) som ritar en kvadrat med angiven sida. Låt första sidan
# ritas i den aktuella riktning sköldpaddan har

from turtle import *


def move(turt, posx, posy):
    turt.penup()
    turt.goto(posx, posy)
    turt.pendown()
    return()

Turtle1 = Turtle()
Turtle2 = Turtle()
Turtle1.speed(4000)
Turtle2.speed(4000)
move(Turtle2, 0, 40)
Turtle1.pencolor("red")
Turtle1.shape("turtle")
Turtle1.forward(120)

Turtle2.pencolor("blue")
Turtle2.shape("turtle")
Turtle2.forward(120)
done()