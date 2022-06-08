def cautare_binara(tab, st, dr, val):
    while st <= dr:
        mij = st + (dr - st) // 2
        if tab[mij] == val:
            return mij
        elif val > tab[mij]:
            st = mij + 1
        else:
            dr = mij - 1
    return -1

if __name__ == '__main__':
    tab = [1, 2, 4, 7, 9]
    val = 7
    st = 0
    dr = 4
    cautare_binara(tab, st, dr, val)