m = int(input("m= "))
n = int(input("n= "))
a = []


def sa(a, i, j):
    maxim = True
    minim = True
    for k in range(0, n):
        if a[i][k] < a[i][j]:
            minim = False
    for k in range(0, m):
        if a[k][j] > a[i][j]:
            maxim = False
    if minim and maxim:
        return True
    else:
        return False


print("Dati matricea a")
for i in range(0, m):
    linie = []
    for j in range(0, n):
        print('a[', i, j, ']= ')
        linie.append(int(input()))
    a.append(linie)
print("matricea a este")
for linie in a:
    print(linie)
print("punctele SA se afla pe pozitiile", end=" ")
for i in range(0, m):
    for j in range(0, n):
        if sa(a, i, j):
            print("(", i, ",", j, ")", end=" ")
