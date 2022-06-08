n = int(input())
aux_n = n
lista_cifa_n = []
while aux_n != 0:
    lista_cifa_n.append(aux_n % 10)
    aux_n //= 10
n_linii_coloane = len(lista_cifa_n)
matrice = []
for i in range(n_linii_coloane):
    matrice.append(lista_cifa_n)
for i in range(n_linii_coloane):
    for j in range(len(lista_cifa_n)):
        print(matrice[i][j], end=' ')
    print()
