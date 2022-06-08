"""Se dă o matrice cu n linii și m coloane și elemente numere întregi. Să se determine, pentru fiecare linie a
matricei, valoarea maximă și indicele coloanei pe care se află valoarea maximă. """


n = int(input("n="))
m = int(input("m="))
matrice = []
for i in range(n):
    linie = []
    for j in range(m):
        linie.append(int(input()))
    matrice.append(linie)
for i in range(n):
    print(max(matrice[i]), end=" ")
    print(matrice[i].index(max(matrice[i])))