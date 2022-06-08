"""Suma nr prime mai mici decat un numar n."""
from math import sqrt


def prim(p):
    nr_prim = True
    for contor in range(2, int(sqrt(p)) + 1):
        if p % contor == 0:
            nr_prim = False
    return nr_prim


if __name__ == '__main__':
    n = int(input("n= "))
    S = 0
    for i in range(2, n):
        if prim(i):
            S += i
    print("Suma prime mai mici ca ", n, 'este', S)
