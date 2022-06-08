def ex_50(n):
    suma = 0
    produs = 1
    for i in range(1, n + 1):
        produs *= i
        suma += produs
    print(suma)


if __name__ == '__main__':
    n = 4
    ex_50(n)