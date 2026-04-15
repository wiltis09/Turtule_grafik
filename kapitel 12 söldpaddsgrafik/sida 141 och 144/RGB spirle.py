# Kapitel 12 – Sköldpaddsgrafik
# Ritar en enkel spiral med turtle.

from turtle import *
import random

speed(0)
offset = int(0)

pencolor("red")
for i in range(0,500):
    for r in range(0,4):
        forward(i)
        left(91)
done()



