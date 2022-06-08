def ordonare_impar_par(lista):
    ordonat = False
    while not ordonat:
        ordonat = True
        for contor in range(0, len(lista)-1):
            if lista[contor]%2==0 and lista[contor+1]%2!=0:
                auxiliar = lista[contor]
                lista[contor] = lista [contor+1]
                lista[contor+1] = auxiliar
                ordonat = False
        if ordonat:
            break
    print(lista)

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    ordonare_impar_par(lista)
