from math import *


def prim(p):
    nr_prim = True
    for contor in range(2, int(sqrt(p)) + 1):
        if p % contor == 0:
            nr_prim = False
    return nr_prim


def ordonare_nr_prime(lista, nr_elemente_lista):
    ordonat = False
    while not ordonat:
        ordonat = True
        for i in range(0, nr_elemente_lista):
            if (prim(lista[i]) == False) and prim(lista[i + 1]) == True:
                print(lista[i], lista[i + 1])
                aux = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = aux
                ordonat = False
        if ordonat:
            break
    print(lista)


if __name__ == '__main__':
    n = 6
    lista = [1, 10, 12, 2, 3, 4, 5]
    ordonare_nr_prime(lista, n)
