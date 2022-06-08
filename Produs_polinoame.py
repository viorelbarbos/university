"""Produsul a doua polinoame."""
m = int(input("m="))
n = int(input("n="))
P = []
Q = []
R = [] #polinomul produs
for i in range(0, m+1):
    print("P[", i, "]=", end=" ")
    P.append(int(input()))
for j in range(0, n+1):
    print("Q[", j, "]=", end=" ")
    Q.append(int(input()))
for j in range(0, m+n+1):
    R.append(0)
for i in range(0, m+1):
    for j in range(0, n+1):
        R[i+j] = R[i+j]+P[i]*Q[i]
print("Polinomul P este", P)
print("Polinomul Q este", Q)
print("Polinomul R este", R)