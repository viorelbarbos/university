linie = []
matrice = []
n = int(input())
for i in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
suma_dp = 0
suma_ds = 0
for i in range(n):
    for j in range(n):
        if i == j:
            suma_dp += matrice[i][j]
        if i + j == n - 1:
            suma_ds += matrice[i][j]
if suma_dp > suma_ds:
    print(suma_dp - suma_ds)
else:
    print(suma_ds - suma_dp)