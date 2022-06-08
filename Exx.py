from graphics import *


def main():
    win = GraphWin("Bilet 10 - Barbos Viorel", 500, 500)
    win.setCoords(0, 0, 500, 500)
    B = Point(100, 150)
    A = Point(100, 350)
    C = Point(400, 150)
    D = Point(400, 350)
    ABCD = Polygon(A, B, C, D)
    ABCD.setFill('yellow')
    ABCD.setWidth(3)
    ABCD.setOutline('red')
    diag_AC = Line(A, C)
    diag_BD = Line(B, D)
    diag_BD.setWidth(3)
    diag_AC.setWidth(3)
    ABCD.draw(win)
    diag_AC.draw(win)
    diag_BD.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()