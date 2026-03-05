from turtle import *


speed(0)
setup(400,400, 0, 0)
setworldcoordinates(0,0,400,400)


def cirkel_1(radie = 0):
    penup()
    goto(xcor(), ycor() - radie) 
    pendown()
    circle(radie)
    penup()
    goto(xcor(), ycor() + radie) 
for i in range(0, 30):

cirkel_1(100)

done()

