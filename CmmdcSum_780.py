linie = []
matrice = []
n = int(input())
for i in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
suma_sus = 0
suma_jos = 0
for i in range(n):
    for j in range(n):
        if i < j:
            suma_sus += matrice[i][j]
        if i > j:
            suma_jos += matrice[i][j]
while suma_sus != suma_jos:
    if suma_sus > suma_jos:
        suma_sus -= suma_jos
    else:
        suma_jos -= suma_sus
print(suma_jos)