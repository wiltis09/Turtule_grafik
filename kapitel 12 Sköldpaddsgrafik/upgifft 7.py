# Gör en funktion kvadrat(sida) som ritar en kvadrat med angiven sida. Låt första sidan
# ritas i den aktuella riktning sköldpaddan har

from turtle import *


speed(0)
setup(400,400, 0, 0)
setworldcoordinates(0,0,400,400)

def kvadrat(sida = 0):
    for i in range(0,4):
        forward(sida)
        left(90)
kvadrat(200)


   

done()

