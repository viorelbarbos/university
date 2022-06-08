n = int(input())
lista = [0 for i in range(100)]
nr_perechi = 0
for i in range(n):
    numar = int(input())
    lista[numar] += 1
for i in range(100):
    nr_perechi += lista[i] // 2
print(nr_perechi)
