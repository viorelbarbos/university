graphics import *
def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Circle(Point(500, 500), 400)
    c.draw(win)
    win.getMouse() #pause for click in window
    win.close()
main()
print()