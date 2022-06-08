n = int(input())
lista = list(map(int, input().split()))
indice_element_maxim = 0
indice_element_minim =0
for i in range(n):
    if lista[i] == min(lista):
        indice_element_minim = i
    elif lista[i] == max(lista):
        indice_element_maxim = i
print(indice_element_minim, indice_element_maxim)