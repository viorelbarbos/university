from graphics import *


def main():
    win = GraphWin("My Circle", 500, 500)
    win.setCoords(0, 0, 500, 500)
    A = Point(100, 350)
    B = Point(100, 150)
    C = Point(400, 150)
    D = Point(400, 350)
    ABCD = Polygon(A, B, C, D)
    ABCD.setFill("yellow")
    ABCD.setWidth(4)
    ABCD.setOutline("red")
    AC = Line(A, C)
    BD = Line(B, D)
    AC.draw(win)
    BD.draw(win)
    ABCD.draw(win)
    win.getMouse()
    win.close()
main()
