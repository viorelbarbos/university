n = int(input())
matrice = []
for i in range(n):
    lista = []
    for j in range(n):
        if i == j or (i + j == n - 1):
            lista.append(0)
        elif i < j and (i + j < n - 1):
            lista.append(1)
        elif i > j and (i + j > n - 1):
            lista.append(2)
        elif i > j and (i + j < n - 1):
            lista.append(3)
        elif i < j and (i + j > n - 1):
            lista.append(3)
    matrice.append(lista)
for i in range(n):
    for j in range(n):
        print(matrice[i][j], end=' ')
    print()
