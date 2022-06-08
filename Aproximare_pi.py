""" Un procedeu aleator pentru aproximarea lui pi """

from graphics import *
from math import sqrt,pi
from random import uniform
n = int(input("numar puncte: "))
win = GraphWin("Un procedeu aleator pentru aproximarea lui pi" ,500,500)
win.setCoords(0.0, 0.0, 500.0, 500.0)
cerc = Circle(Point(250,250),200)
A = Point(50,450)
B = Point(50,50)
C = Point(450,50)
D = Point(450,450)
patrat = Polygon(A,B,C,D,A)
patrat.setWidth(3)
cerc.setWidth(3)
patrat.setOutline("red")
cerc.setOutline("blue")
cerc.draw(win)
patrat.draw(win)
interior = 0
i = 0
while i <= n:
    x = uniform(-1,1)
    y = uniform(-1,1)
    dist = sqrt(x**2+y**2)
    if dist <= 1:
        interior = interior + 1
        P = Point(int(250+200*x),int(250+200*y))
        P.setOutline("red")
        P.draw(win)
    else:
        P = Point(int(250 + 200 * x), int(250 + 200 * y))
        P.setOutline("black")
        P.draw(win)
    i = i + 1
PI = 4. * interior / n
message = Text(Point(120, 470), "Valoarea  lui pi este: 3.14159")
message.draw(win)
message1 = Text(Point(150, 20), "Valoarea aproximata a lui pi este: " + str(PI))
message1.draw(win)
win.getMouse()
win.close()
