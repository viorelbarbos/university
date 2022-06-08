def cautare_binara(lista, st, dr, val):
    while st <= dr:
        mij = st + (dr - st) // 2
        if lista[mij] == val:
            return 1
        elif val > lista[mij]:
            st = mij + 1
        else:
            dr = mij - 1
    return 0


n = int(input())
lista1 = list(map(int, input().split())) # 1 2 0 3
m = int(input())
lista2 = list(map(int, input().split())) # 1 2 6
for j in range(m):
    st = 0
    dr = n - 1
    print(cautare_binara(lista1, st, dr, lista2[j]), end=' ')