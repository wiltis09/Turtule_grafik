from turtle import *

shapes = [ "arrow", "turtle", "circle", "square", "triangle"]

back(300)
fillcolor("green")
stamps = []
turtlesize(4,2,3)
for sh in shapes:
    fd(100)
    shape(sh)
    h = stamp()
    stamps.append(h)
clearstamp(stamps[2])
done()



