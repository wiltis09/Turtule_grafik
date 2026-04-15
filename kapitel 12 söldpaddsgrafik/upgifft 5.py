# Tänk en punkt på x-axeln och en på y-axeln och låt punkterna förflytta sig så att den på x-
# axeln stegas in mot origo och dne på y-axeln flyttas uppåt med samma steglängd. Dra en
# linje mellan punkterna för varje segning. (Använd funktionen från föregåend uppgift.) Du
# bör då få en figur ungefär som denna:


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

