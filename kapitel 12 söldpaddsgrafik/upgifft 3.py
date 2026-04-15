
# Gör en funktion line(x1, y1, x2, y2) vilken tar två punkter som parametrar och
# som
#
# lyfter pennan
# går till punkt p1 (med kordinaterna (x1, y1)) 
# sätter ner pennan 
# går till punkt p2 (med kordinaterna (x2, y2)) 
# lyfter pennan

# Skala sedan om fönstret med kommandot setworldcoordinates(-10, -10, 10, 10) samt 
# använd den skapade funktionen till att loppa och ruta upp skärmen med ett rutnät som är 
# 20 x 20 rutor.


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
done
