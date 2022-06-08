n = int(input())
lista = list(map(int, input().split()))
lista_frecventa = [0 for i in range(100000)]
for i in range(n):
    lista_frecventa[lista[i]] += 1
print(lista_frecventa)
for i in range(100000):
    if lista_frecventa[i] != 0:
        print(i, end=' ')

