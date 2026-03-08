from turtle import *
import random

speed(0)
offset = int(12)
def drew_box(size, tilt):
    left(tilt)
    forward(size)
    left(tilt)
    forward(size)
    left(tilt)
    forward(size)
    left(tilt)
    forward(size)
for k in range(16):
    pendown()
    forward(70)
    for i in range(10):
        drew_box(30,90)
        forward(12)
        left(12)
    penup()
    goto(0,0)
    home()
    left(offset)
    pendown()
    forward(70)
    for i in range(10):
        drew_box(30,90)
        forward(12)
        right(12)
    offset += 12
    penup()
    
    
     
done()



