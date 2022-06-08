def afisare_cuvinte_vocale():
    sir = input()
    sir = sir + ' '
    ok = 0
    n = len(sir)
    i = 0
    inceput = 0
    consoana = 0
    for i in range(0, n):
        if sir[i] != ' ':
            if sir[i] == 'a' or sir[i] == 'e' or sir[i] == 'i' or sir[i] == 'o' or sir[i] == 'u':
                ok = 1
            else:
                consoana = 1
        else:
            if ok != 0 and consoana != 1:
                print(sir[inceput:i])
            inceput = i + 1
            ok = 0
            consoana = 0


if __name__ == '__main__':
    afisare_cuvinte_vocale()
