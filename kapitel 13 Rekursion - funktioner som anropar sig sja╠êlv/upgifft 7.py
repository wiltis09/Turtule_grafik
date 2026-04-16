# En typ av fraktal är den så kallade Sierpenskis triangel. Man utgår från att rita upp en 
# liksidig (fylld) triangel.

# Man kan tänka sig denna triangel uppbyggd av tre andra, och liksom "skär ut" en triangel i 
# mitten som alltså inte ritas när de andra ritas:

from turtle import *


speed(0)
offset = int(0)
setworldcoordinates(0,0,10,10)
fillcolor("red")

def line(x1, y1, x2, y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)
    penup()
for i in range(0,10):
    line(0,offset,10,offset)
    line(offset,0,offset,10)
    offset += 1
def fillcoloer_on_click(x, y):
    
    penup()
    print(x, y, "pos")
    if x < 0 and x > 10:
        if y < 0 and y > 10:
            return
            print("bad")
    #box_x = int(x  / 10) * 10
    #box_y = int(y / 10) * 10
     
    box_x = int(x) 
    box_y = int(y) 


    print(box_x, box_y, "box_pos")
    print((x * 10), (y * 10), "box_pos")
    goto(box_x, box_y)

    pendown()
    begin_fill()
    for i in range(0,4):
        forward(1)
        left(90)
    end_fill()

    
    #circle(10)
    


    


    end_fill()

onscreenclick(fillcoloer_on_click)

done()

