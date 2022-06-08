n = int(input())
lista_valori = list(map(int, input().split()))
st = 0
dr = 0
lungime_maxima = 0
lungime_variabila = 0
i = 0
for i in range(n):
    if lista_valori[i] == 0:
        lungime_variabila += 1
    else:
        if lungime_maxima < lungime_variabila:
            lungime_maxima = lungime_variabila
            dr = i-1
            st = dr - lungime_variabila + 1
            lungime_variabila = 0
if lungime_maxima < lungime_variabila:
    lungime_maxima = lungime_variabila
    dr = i
    st = dr - (lungime_variabila - 1)
    lungime_variabila = 0
if dr == st:
    print(st + 1)
else:
    print(st + 1, dr + 1)