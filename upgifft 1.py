from turtle import *
speed(0)
tracer(25)

color("red", "yellow")  
def rita_en_sylt(size = int, x_pos = int, y_pos = int ):
   Turtle.fillcolor = color("red")
   begin_fill()
   penup()
   goto(x_pos, y_pos)
   pendown()
   Turtle.fillcolor = color("red")
   diameter_big = size * 2
   diameter_small = diameter_big - ((size * 0.30) * 2)
   print("klp", diameter_big, diameter_small)
   ofset = (diameter_big - diameter_small )/ 2
   print("klp", diameter_big, diameter_small,)
   circle(size)
   end_fill()
   penup()
   goto(x_pos, (y_pos + ofset))
   pendown()
   begin_fill()
   Turtle.fillcolor = color("yellow")
   circle(size - (size * 0.30))
   end_fill()
rita_en_sylt(60, 0, 0)
hideturtle()
done()
