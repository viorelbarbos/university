n = int(input())
lista = list(map(int, input().split()))
lista_cifre = [0 for i in range(10)]
for i in range(n):
    aux = lista[i]
    while aux != 0:
        lista_cifre[aux % 10] += 1
        aux //= 10
dictionar = {}
for i in range(10):
    aux_dictionar = {i: lista_cifre[i]}
    dictionar.update(aux_dictionar)
dictionar = {k: v for k, v in sorted(dictionar.items(), key=lambda item: item[1])}
for key in dictionar:
    if dictionar[key] != 0:
        print(key, end=' ')