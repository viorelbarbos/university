"""Să se scrie o funcție C++ cu următorul prototip:
care primește ca parametru un număr natural nenul n și returnează cel mai mic număr natural,
 strict mai mare decât n, care are în reprezentarea în baza 2 același număr de biți de 1 ca și n."""


def ex_2620(numar):
    auxiliar = numar
    numar_baza2 = []
    numar1_baza2 = []
    while auxiliar != 0:
        numar_baza2.append(auxiliar % 2)
        auxiliar //= 2
    for numar1 in range(numar + 1, 99):
        auxiliar = numar1
        while auxiliar != 0:
            numar1_baza2.append(auxiliar % 2)
            auxiliar //= 2
        if numar_baza2.count(1) == numar1_baza2.count(1):
            return numar1
        else:
            numar1_baza2 = []


if __name__ == '__main__':
    n = 30
    print(ex_2620(n))
