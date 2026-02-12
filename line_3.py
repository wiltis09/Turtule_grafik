from turtle import *
speed(900)
def line(x1, y1, x2, y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)
    penup()
    
def drew_rutnät(box_size, ofset):
    for i in range(60):

        ofset += 20
        line(ofset, -500, ofset, 500)
        line(-500, ofset, 500, ofset)

drew_rutnät(0, -500)
#setworldcoordinates(-10,-10,10,10)
done()
