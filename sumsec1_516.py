def cautare_din_fata(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 1:
            return i
    return -1


def cautare_din_spate(lista):
    for j in range(len(lista) - 1, -1, -1):
        if lista[j] % 2 == 1:
            return j
    return -1


if __name__ == '__main__':
    n = int(input())
    lista_valori = list(map(int, input().split()))
    index_fata = cautare_din_fata(lista_valori)
    index_spate = cautare_din_spate(lista_valori)
    if index_spate == index_fata:
        print(lista_valori[index_spate])
    else:
        Suma = 0
        for j in range(index_fata, index_spate + 1):
            Suma += lista_valori[j]
        print(Suma)
