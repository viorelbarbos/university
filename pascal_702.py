nr_randuri = int(input())
nr_de_gasit_multipi = int(input())
#  4
lista = [ 0 for i in range(nr_randuri+1)]
lista[4] = 1
matrice = []
matrice.append(lista)
for i in range(nr_randuri+1):
    lista_auxiliara = []
    for j in range(nr_randuri+1):
        lista_auxiliara.append(lista[j] + lista[j+1])
    matrice.append(lista_auxiliara)
    lista = lista_auxiliara
for i in range(nr_randuri):
    for j in range(nr_randuri):
        print(matrice[i][j], end=' ')
    print()