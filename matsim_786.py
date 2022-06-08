linie = []
matrice = []
n = int(input())
for i in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
for i in range(n):
    for j in range(n):
        if i > j:
            aux = matrice[i][j]
            matrice[i][j] = matrice[j][i]
            matrice[j][i] = aux
for i in range(n):
    for j in range(n):
        print(matrice[i][j], end=' ')
    print()