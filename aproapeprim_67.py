"""Să se scrie o funcție C++ care verifică dacă un număr natural transmis ca parametru este aproape prim.
 Un număr natural este aproape prim dacă se poate scrie ca produs de două numere prime distincte."""


def prim(p):
    nr_prim = True
    if p == 1 or p == 0:
        nr_prim = False
        return nr_prim
    for contor in range(2, p // 2):
        if p % contor == 0:
            nr_prim = False
    return nr_prim


def ex_67(n):
    for divizor1 in range(2, int(n ** 1 / 2) + 1):
        for divizor2 in range(divizor1 + 1, int(n ** 1 / 2) + 1):
            print(divizor1, " ", divizor2, end='\n')
            if prim(divizor1) and prim(divizor2):
                if divizor1 * divizor2 == n:
                    return 1
    return 0


if __name__ == '__main__':
    print(ex_67(21))
