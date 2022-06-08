def ex_2329(index, lista_elemente):
    numere_prime = 0 # orice numaratoare incepe de la 0
    for i in range(0, index - 1): # parcurgem lista pana la penultimul element
        for j in range(i + 1, index): # parcurgem lista pana la ultimul element
            ok = 0 # folosim ok pentru a verifica daca numarul este prim
            suma = 0 # initializam suma cu 0 de fiecare data
            suma = lista_elemente[i] + lista_elemente[j] # adunam elementul de pe pozitia i cu elementele de pe pozitia j
            if suma == 2: # daca suma este 2 inseamna ca numarul nu este prim
                ok = 1
            else: # daca numarul nu este 2 parcurgem urmatoarea secventa
                for divizor in range(2, suma): # test de prim in care verificam daca numarul se poate imparti
                    if suma % divizor == 0: # testam daca are divizori
                        ok = 1 # daca gasim un divizor ok devine 1 pentru a cunoaste ca numarul nu este prim
                        break # acest break forteaza structura repetitiva sa se opreasca
            if ok != 1: # daca ok este 1 atunci numarul nu este prim
                numere_prime += 1 # daca ok este 0 atunci numarul este prim deci putem sa-l numaram
    print(numere_prime)


if __name__ == "__main__":
    n = int(input())
    lista = []
    for i in range(0, n):
        x = int(input("Adaugati un numar la lista "))
        lista.append(x)
    ex_2329(n, lista)
