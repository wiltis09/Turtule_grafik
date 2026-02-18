from turtle import *


speed(0)
setup(400,400, 0, 0)
setworldcoordinates(0,0,400,400)
def line(x1, y1, x2, y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)
    penup()

offset = 0
for i in range(0, 200 + 10, 10):

    offset += 0
    line(i, offset, offset, (200 - i))

done()

