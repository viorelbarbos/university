"""Test animatie disc"""
from graphics import *
import time


def moveAll(ListaFiguri, dx, dy):
    for figura in ListaFiguri:
        figura.move(dx, dy)


def moveALLOnline(ListaFiguri, dx, dy, repetitii, delay):
    for i in range(repetitii):
        moveAll(ListaFiguri, dx, dy)
        time.sleep(delay)


def main():
    win = GraphWin("Animatie disc", 500, 500)
    win.setCoords(0, 0, 500, 500)
    cerc = Circle(Point(250, 250), 50)
    cerc.setOutline("green")  # linia
    cerc.setFill("orange")  # umplere
    cerc.setWidth(3)  # ingrosare
    cerc.draw(win)
    dreptunghi = Rectangle(Point(100, 300), Point(200, 280))
    dreptunghi.setFill("red")
    dreptunghi.draw(win)
    ListaFiguri = [cerc, dreptunghi]
    for i in range(3):
        moveALLOnline(ListaFiguri, 5, 0, 10, 0.02)
        moveALLOnline(ListaFiguri, 0, 5, 10, 0.02)
        moveALLOnline(ListaFiguri, -5, 0, 10, 0.02)
        moveALLOnline(ListaFiguri, 0, -5, 10, 0.02)
    win.getMouse()
    win.close()

main()