from turtle import *
import random

colormode(255)  # allow RGB values from 0–255

for i in range(random.randint(0,255)):
    speed(0)
    color = (random.randint(0,255),
             random.randint(0,255),
             random.randint(0,255))
    pos = (random.randint(-255,255),
             random.randint(-255,255))
    size = random.randint(10,100)
    penup()
    goto(pos)
    pendown()
    dot(size, color)

done()
