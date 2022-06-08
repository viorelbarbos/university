linie = []
matrice = []
n = int(input())
zona = int(input())
for i in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
zona_nord, zona_sud, zona_est, zona_vest = 0, 0, 0, 0
if zona == 1:
    for i in range(n):
        for j in range(n):
            if i < j and i + j < n - 1:
                zona_nord += matrice[i][j]
    print(zona_nord)
elif zona == 3:
    for i in range(n):
        for j in range(n):
            if i > j and i + j > n - 1:
                zona_sud += matrice[i][j]
    print(zona_sud)
elif zona == 4:
    for i in range(n):
        for j in range(n):
            if i > j and i + j < n - 1:
                zona_vest += matrice[i][j]
    print(zona_vest)
else:
    for i in range(n):
        for j in range(n):
            if i < j and i + j > n - 1:
                zona_est += matrice[i][j]
    print(zona_est)