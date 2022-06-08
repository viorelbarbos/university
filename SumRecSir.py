"""Calculul sumei S = 1 + 2 +3 + 4 + ... + n cu functie recursiva."""


def sumrec(numar):
    if numar == 1:
        return 1
    else:
        return numar + sumrec(numar - 1)


if __name__ == '__main__':
    n = eval(input("n="))
    print("Suma este", sumrec(n))
