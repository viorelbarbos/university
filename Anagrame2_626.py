fisier = open("anagrame2.in", 'r')
prima_linie = fisier.readline()
p = int(prima_linie)
string = fisier.readline()
cuvant = fisier.readline()
fisier.close()
scriere_fisier = open("anagrame2.out", "w")
if p == 1:
    ok = True
    lungime_cuvant = len(cuvant)
    i = 0
    contor = 0
    while ok:
        auxiliar = ""
        for j in range(0, lungime_cuvant):
            auxiliar = auxiliar + string[i]
            i += 1
        contor += 1
        if sorted(cuvant) == sorted(auxiliar):
            ok = False
            scriere_fisier.write(auxiliar)
        i = contor
if p == 2:
    lungime_cuvant = len(cuvant)
    i = 0
    contor = 0
    nr_anagrame = 0
    while i < len(string) - (lungime_cuvant - 1):
        auxiliar = ""
        for j in range(0, lungime_cuvant):
            auxiliar = auxiliar + string[i]
            i += 1
        contor += 1
        if sorted(cuvant) == sorted(auxiliar):
            nr_anagrame += 1
        i = contor
    scriere_fisier.write(str(nr_anagrame))
scriere_fisier.close()