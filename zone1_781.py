linie = []
matrice = []
n = int(input())
for i in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
zona_nord, zona_sud, zona_est, zona_vest = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if i < j and i + j < n - 1:
            zona_nord += matrice[i][j]
        if i > j and i + j > n - 1:
            zona_sud += matrice[i][j]
        if i > j and i + j < n - 1:
            zona_vest += matrice[i][j]
        if i < j and i + j > n - 1:
            zona_est += matrice[i][j]

lista = [zona_est, zona_vest, zona_nord, zona_sud]
lista = sorted(lista)
for element in lista:
    print(element, end=' ')
