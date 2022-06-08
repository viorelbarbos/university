m = int(input("m= "))
n = int(input("n= "))
a = []
b = []
v = []
for k in range(0, m*n):
    v.append(0)
for i in range(0, m):
    linie = []
    for k in range(0, m):
        print('a[', i, k, ']=')
        linie.append(int(input()))
    a.append(linie)
for i in range(0, m):
    linie = []
    for k in range(0, m):
        print('b[', i, k, ']=')
        linie.append(int(input()))
    b.append(linie)
print('a= ')
print(a)
print('b= ')
print(b)
for i in range(0, m):
    for k in range(0, n):
        v[b[i][k]] = a[i][k]
print("Elementle matricii A dupa ordinea data de B sunt:")
print(v)
