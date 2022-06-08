"""Determinarea maximului unui sir de numere cu ajutorul recursivitatii."""


def maxrec(lista, n):
    if n == 0:
        return lista[n]
    else:
        if maxrec(lista, n - 1) >= lista[n]:
            return maxrec(lista, n - 1)
        else:
            return lista[n]


if __name__ == '__main__':
    a = [1, 2, 5, 3 ,10, 1]
    n = 6
    print(maxrec(a, n))