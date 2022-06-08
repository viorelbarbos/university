def ex_0294():
    numar_elemente = int(input())
    if numar_elemente > 100:
        print(" ")
    else:
        sir_numere = input()
        lista_auxiliara = sir_numere.split()
        primul_nr_din_sir = int(lista_auxiliara[0])
        oglindit = 0
        ok = 0
        while primul_nr_din_sir > 0:
            oglindit = oglindit * 10 + primul_nr_din_sir % 10
            primul_nr_din_sir //= 10
        for i in range(1, numar_elemente):
            if oglindit == int(lista_auxiliara[i]):
                ok = 1
        if ok == 1:
            print("DA")
        else:
            print("NU")


if __name__ == "__main__":
    ex_0294()
