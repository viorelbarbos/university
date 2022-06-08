n = int(input())
lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
numar_iteratii = 0
for i in range(n):
    if lista1[i] == 1 and lista2[i] == 2:
        lista1[i] = 2
        lista2[i] = 1
        numar_iteratii += 1
    elif lista1[i] == 2 and lista2[i] == 1:
        lista1[i] = 1
        lista2[i] = 2
        numar_iteratii += 1
print(numar_iteratii)