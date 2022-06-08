""" Desenare segmente aleatoare de culori aleatoare pana la clic de mouse"""

from graphics import *
from random import *
import time
def alege_culoare():
    culori = ["blue","black","brown","red","yellow","green","orange","magenta","turquoise","pink"]
    shuffle(culori)
    return culori[0]
win = GraphWin("Segmente aleatoare" ,500,500)
win.setCoords(0.0, 0.0, 500.0, 500.0)
while True:
    x1 = int(uniform(0, 500))
    y1 = int(uniform(0, 500))
    x2 = int(uniform(0, 500))
    y2 = int(uniform(0, 500))
    Linie = Line(Point(x1, y1), Point(x2, y2))
    c = alege_culoare()
    Linie.setOutline(c)
    Linie.setWidth(5)
    Linie.draw(win)
    time.sleep(0.03)                # Asteapta 0.03 secunde
    if win.checkMouse()!= None:     # Verifica daca s-a dat clic de mouse. Daca da, se incheie
        break
win.close()