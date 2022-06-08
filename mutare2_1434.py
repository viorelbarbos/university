


def prim(p):
    nr_prim = True
    if p == 1 or p == 0:
        nr_prim = False
        return nr_prim
    for contor in range(2, p // 2):
        if p % contor == 0:
            nr_prim = False
    return nr_prim


def ordonare_nr_prime(lista, nr_elemente_lista):
    ordonat = False
    while not ordonat:
        ordonat = True
        for i in range(0, nr_elemente_lista):
            if not prim(lista[i]) and prim(lista[i + 1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordonat = False
    print(lista)


if __name__ == '__main__':
    n = 6
    lista = [1, 0, 7, 10, 12, 2, 3, 4, 5]
    ordonare_nr_prime(lista, n)
