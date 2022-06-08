# n = int(input())
i = 0
lista = [5, 4, 1, 3, 2]
# for i in range(0, n):
# x = int(input())
# lista.append(x)
ordonat = False
while not ordonat:
    ordonat = True
    for i in range(0, len(lista) - 1):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
            print(lista[i], end=" ")
            ordonat = False
    if ordonat:
        break
print(lista)
