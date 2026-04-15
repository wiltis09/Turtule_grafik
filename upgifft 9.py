# Om du kan lite trigonometri kan du försöka rita alla digonaler i en n-hörning. Här ett
# exampel med en 17-hörning:

# Använd setworldcoordinates() och räkna först ut koordinaterna för alla
# hörpunkter. De ligger ju på en cirkel med viss radie och med en viss vinkel mellan varje
# punkt. Hörnen har alltså koordinaterna

#                   ( i * 2pi)          
#          xi = cos ----------
#                   (   n    )

#                   ( i * 2pi)          
#          yi = sin ----------
#                   (   n    )

# När diagonalerna ritas, se då till att ine varje linje behöver ritas två gånger


from turtle import *



speed(0)
setup(400,400, 0, 0)
setworldcoordinates(0,0,400,400)


