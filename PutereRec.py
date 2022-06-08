"""Calculul lui a la puterea n prin funtie recursiva."""


def putere(a, n):
    if n == 0:
        return 1
    else:
        return a*putere(a, n-1)


if __name__ == '__main__':
    a = int(input())
    n = int(input())
    print(a, "la puterea", n, "este", putere(a, n))
    print("Verificare cu ** ", a**n)