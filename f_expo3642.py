"""Subprogramul furnizează rezultatul tot prin intermediul tabloului a. Pentru fiecare element a[i], i=0..n-1
, se calculează exponentul maxim e cu proprietatea că 2**e ≤ a[i], iar rezultatul se va memora tot în a[i]
Dacă n=6, a=(9,1,5,15,19,30), după apel a=(3,0,2,3,4,4)."""


def ex_3642(lista, elemente_lista):
    for i in range(0, elemente_lista):
        e = 0 # initializam exponentul cu 0
        while 2 ** e < lista[i]: # cat timp 2 la puterea e este mai mic decat elementul din lista
            e += 1 # marim cu 1 exponentul
        if 2 ** e > lista[i]: # daca 2 la puterea e este mai mare decat elementul din lista
            e -= 1 # il scadem (vezi elementul 5 din lista cum se parcurge prin functie)
            lista[i] = e # adaugam exponentul in lista in locul elementului
        else:
            lista[i] = e # daca 2 la puterea e nu este mai mare decat acel element, se adauga direct

    print(lista)


if __name__ == '__main__':
    v = [9, 1, 5, 15, 19, 30]
    n = 6
    ex_3642(v, n)
