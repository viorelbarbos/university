"""Se dă o matrice cu n linii şi m coloane şi elemente numere naturale.
 Determinați suma valorilor pare din matrice."""

if __name__ == '__main__':
    n = int(input("n="))  # citim de la tastatura numarul de linii pe care le va avea matricea
    m = int(input("m="))  # citim de la tastatura numarul de coloane pe care le va avea matricea
    matrice = []  # initializam o matrice fara elemente
    for i in range(n):
        linie = []  # intializam linia noua
        for j in range(m):
            print("matrice[", i, "][", j, "]=")
            linie.append(int(input()))  # citim elementele de pe linie
        matrice.append(linie)  # lipim linia la matrice
    suma_el_pare = 0  # initializam suma elementelor  pare cu 0
    for i in range(n):  # parcurgem matricea linie cu linie
        for j in range(m):
            if matrice[i][j] % 2 == 0:  # verificam daca elementul este par
                suma_el_pare += matrice[i][j]  # daca gasim un element par il adunam
    print("Suma elementelor pare din matrice este", suma_el_pare)  # afisam suma elementelor pare
    for i in range(n):
        for j in range(m):
            print(matrice[i][j], end=" ")
        print()
