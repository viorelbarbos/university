n = int(input("n="))  # citim de la tastatura numarul de linii pe care le va avea matricea
m = int(input("m="))  # citim de la tastatura numarul de coloane pe care le va avea matricea
matrice = []  # initializam o matrice fara elemente
vector_sume = []  # initializam o lista unde o sa adaugam suma fiecarei linii
for i in range(n):
    linie = []  # intializam linia noua
    suma_linie = 0  # initializam suma elementelor de pe linie cu 0
    maxim_linie = -1  # initializam maximul de pe linie cu -1
    for j in range(m):
        print("matrice[", i, "][", j, "]=")
        linie.append(int(input()))  # citim elementele de pe linie
        suma_linie += linie[j]  # adaugam elementul citit de la tastatura la suma elementelor de pe linie
        if linie[j] > maxim_linie:  # totodata gasim maximul de pe linie
            maxim_linie = linie[j]
    matrice.append(linie)  # lipim linia la matrice
    vector_sume.append(suma_linie - maxim_linie)  # adaugam suma el de pe linie minus cel mai mare el de pe linie
print(vector_sume)
