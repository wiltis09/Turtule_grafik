# Bygg sedan på programmet så att det ritar samma sak i alla kvadranterna:

# Lägg märke till att fastän linjer är räta så bildas det en båglinje som liksom innesluter
# alla linjerna. En sådan yttre kurva som innesluter en kurskara kallas envelop.

from turtle import *


speed(0)
setup(400,400, 0, 0)
tracer(0, 0)
setworldcoordinates(0,0,400,400)
def line(x1, y1, x2, y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)
    penup()



for i in range(0, 200 + 10, 10):

    a = i
    b = 200 - i

    line(b, 0, 0, a)
    line(-b, 0, 0, a)
    line(-a, 0, 0, -b)
    line(a, 0, 0, -b)


   

done()

