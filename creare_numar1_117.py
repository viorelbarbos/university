def ex_117(lista, n):
    maxim = max(lista)
    minim = min(lista)
    nr_cifre = len(str(minim))
    maxim = maxim * (10**nr_cifre) + minim
    return maxim


if __name__ == '__main__':
    lista = [120, 34, 51, 26, 403, 71]
    n = 6
    print(ex_117(lista, n))