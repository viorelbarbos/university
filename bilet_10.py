"""Desenare dreptunhi si diagonale"""
from graphics import *

win = GraphWin("Bilet 10 - Barbos Viorel", 500, 500)
win.setCoords(0, 0, 500, 500)
A = Point(100, 350)
B = Point(100, 150)
C = Point(400, 150)
D = Point(400, 350)
Diagonala_AC = Line(A, C)
Diagonala_CD = Line(B, D)
dreptunghi = Polygon(A, B, C, D)
dreptunghi.setOutline("red")  # culoare contur
dreptunghi.setWidth(3)  # grosime contur
dreptunghi.setFill("yellow")  # culoare inaontru
dreptunghi.draw(win)
Diagonala_AC.setWidth(3)
Diagonala_CD.setWidth(3)
Diagonala_CD.draw(win)
Diagonala_AC.draw(win)
win.getMouse()
win.close()
