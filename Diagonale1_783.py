linie = []
matrice = []
n = int(input())
for i in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
suma_vecin1 = 0
suma_vecin2 = 0
for i in range(n):
    for j in range(n):
        if j - i == 1:
            suma_vecin1 += matrice[i][j]
        if i - j == 1:
            suma_vecin2 += matrice[i][j]
print(suma_vecin1 + suma_vecin2)
