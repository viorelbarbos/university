""" Desenare discuri aleatoare de raze si culori aleatoare pana la clic de mouse"""

from graphics import *
from random import *
import time
def alege_culoare():
    culori = ["blue","black","brown","red","yellow","green","orange","magenta","turquoise","pink"]
    shuffle(culori)
    return culori[0]
win = GraphWin("Discuri aleatoare" ,500,500)
win.setCoords(0.0, 0.0, 500.0, 500.0)
while True:
    x = int(uniform(0, 500))
    y = int(uniform(0, 500))
    r = int(uniform(0,100))
    cerc = Circle(Point(x, y), r)
    c = alege_culoare()
    cerc.setFill(c)
    cerc.draw(win)
    time.sleep(0.05)                # Asteapta 0.05 secunde
    if win.checkMouse()!= None:     # Verifica daca s-a dat clic de mouse. Daca da, se incheie
        break
win.close()