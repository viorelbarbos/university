"""Produsul a doua polinoame cu coef intregi."""
m = int(input())
n = int(input())
P, Q, R = [], [], []
for i in range(0, m + 1):
    print("P[", i, "]=")
    P.append(int(input()))
for j in range(0, n + 1):
    print("Q[", j, "]=")
    Q.append(int(input()))
for k in range(0, m + n + 1):
    R.append(0)
for i in range(0, m + 1):
    for j in range(0, n + 1):
        R[i + j] = R[i + j] + P[i] * Q[j]
print("Polinomul P este", P)
print("Polinomul P este", Q)
print("Polinomul P este", R)
