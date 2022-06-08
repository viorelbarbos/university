"""Modul propriu exemplu."""
ro =9.8
def Fact(n):
    F = 1
    for i in range(1, n + 1):
        F *= i
    return F


def Sumainv(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / i
    return S

print("utilizarea modulului propriu")