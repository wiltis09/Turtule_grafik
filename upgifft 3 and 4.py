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
    


def drew_grid(box_size, ofset, net_size):
    for i in range(int(net_size / box_size) + 1):
        line(0, ofset, net_size, ofset)
        line(ofset, 0, ofset, net_size)
        ofset += box_size
drew_grid(20, 0, 80)

def fillcoloer_on_click(x, y):
    print(x, y, "pos")
    if x < 0 and x > 80:
        if y < 0 and y > 80:
            return
            print("bad")
    
    box_x = int(x / 20) * 20
    box_y = int(y / 20) * 20

    begin_fill()
    goto(box_x + 10, box_y)
    circle(10)
    


    
    print("tesst", box_x, box_y)
    print("tesst", x, y)

    end_fill()

onscreenclick(fillcoloer_on_click)



done()
