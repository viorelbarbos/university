linie = []
matrice = []
n = int(input())
for i in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
suma_linie = [0 for i in range(n)]
suma_dp = 0
suma_ds = 0
for i in range(n):
    for j in range(n):
        suma_linie[j] += matrice[i][j]
        if i == j:
            suma_dp += matrice[i][j]
        if i + j == n - 1:
            suma_ds += matrice[i][j]
suma_coloane = [0 for i in range(n)]
for j in range(n):
    for i in range(n):
        suma_coloane[i] += matrice[i][j]
ok = False
for i in range(n):
    if suma_linie[i] == suma_coloane[i] == suma_ds == suma_dp:
        ok = True
    else:
        ok = False
        break
if ok:
    print("true")
else:
    print("false")
