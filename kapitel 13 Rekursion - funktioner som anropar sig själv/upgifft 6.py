# Här är ett #träd som du kanske kan rita upp med en rekursiv funktion i Python:

# Trädet behöver inte ha samma vinkel mellan grenarna utan "grenarna" kan ha olika vinklel
# och längd. Dessutom kan linjerna få ha olika tjocklek, avtagande ju djupare man kommer i
# rekustionen och dessutom olika färg så att de grövre är buna och de tunnare gröna

# Om förhållandet mellan fraktal figurer och bildningar i naturen kan du läsa om på
# http://en.wikipedia.org/wiki/L-system
# Däe så kallade Lindenmayersystem eller L-system behandlas



from turtle import *
speed(0)
tracer(0, 0)
penup()
goto(0, -250)   # move to bottom center
pendown()
bgcolor("skyblue")
def draw_tree(size, length, turn, pen_size):
    pensize(max(1, pen_size - 2))
    if size == 0:
        return
    
        # Color changes
    if size <= 8:
        pencolor("green")
    else:
        pencolor("brown")
    forward(length)
    
    left(turn)
    draw_tree(size - 1, length - 10, turn, (pen_size - 1))
    
    right(2 * turn)
    draw_tree(size - 1, length - 10, turn, (pen_size - 1) )
    
    left(turn)
    penup()
    pensize(pen_size + 2)
    backward(length)  # go back to previous position
    pendown()

left(90)
draw_tree(10, 100, 25, 10)

done()