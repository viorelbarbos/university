def ex_35(lista, n):
    k = 0
    for i in range(0, n):
        if sum(lista) / n <= lista[i]:
            k += 1
    if k == 0:
        print("Nu exista numere mai mari ca media aritmetca a listei")
    else:
        print(k)


if __name__ == '__main__':
    a = False
    while a is False:
        n = int(input("n="))
        if n <= 0 or n >= 100:
            a = False
        else:
            a = True
    lista = []
    for i in range(0, n):
        lista.append(eval(input("Adaugati elemente listei:")))
    ex_35(lista, n)