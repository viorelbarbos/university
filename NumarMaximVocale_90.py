fisier = open("vocmax.in", 'r')  # deschidem fisierul de unde dorim sa citim valorile
n = int(fisier.readline())  # citim prima linie care contine numarul de propozitii
max_voc = 0  # initializam o variabila pentru a stii care propozitiie are mai multe vocale
cuvant_max = ""  # initializam o variabila pentru a stoca propozitia cu cele mai mult vocale
for i in range(n):  # parcurgem restul fisierului
    nr_voc = 0  # variabila care stocheaza numarul de vocale pentru cuvantul citit
    cuvant = fisier.readline()  # citim cuvantul din fisier
    for j in range(len(cuvant)):  # parcurgem cuvantul din fisier
        if cuvant[j] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  # daca o litera este vocala o contorizam
            nr_voc += 1
    if nr_voc > max_voc:  # daca numarul de vocale de la propozitia precedenta este mai mare decat numarul maxim de vocale
        max_voc = nr_voc  # memoram numarul maxim de vocale
        cuvant_max = cuvant  # si memoram propozitia cu numarul mai mare de vocale
scriere_fisier = open("vocmax.out", 'w')  # deschidem fisierul unde dorim sa scriem valorile
scriere_fisier.write(cuvant_max)  # scriem in fisier propozitia cu numarul maxim de vocale
scriere_fisier.close()  # inchidem cele doua fisiere
fisier.close()
