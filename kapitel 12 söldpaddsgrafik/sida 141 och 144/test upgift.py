# Kapitel 12 – Sköldpaddsgrafik
# Testprogram som ritar punkter utifrån sinusfunktionen.

from turtle import *
from math import *

speed(0)
offset = int(0)
pencolor("red")
pensize(1)
fillcolor("red")


for x in range(0,1000, 10):
 goto(x , sin(x))
done()



