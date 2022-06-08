"""Calcului aproximativ a lui radical din a, folosind un sir recurent
convergent la radical din a."""
from math import *
while True:
    a = eval(input("a= "))
    if a > 0:
        break
while True:
    eps = eval(input("eps= "))
    if eps > 0:
        break
x = a
y = 1 / 2 * (x + a / x)
while abs(y-x) >= eps:
    x = y
    y = 1 / 2 * (x + a / x)
print("Radical aproximativ = ", format(y, '.10f'))
print("Radical cu sqrt = ", format(sqrt(a),'.10f'))

