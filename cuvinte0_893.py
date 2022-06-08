propozitie = input()
propozitie += ' '
cuvant = ""
propozitie_sortata = []
for i in range(len(propozitie)):
    if propozitie[i] != ' ':
        cuvant += propozitie[i]
    else:
        propozitie_sortata.append(cuvant)
        cuvant = ""
propozitie_sortata = list(dict.fromkeys(propozitie_sortata))
propozitie_sortata = sorted(propozitie_sortata)
for i in range(len(propozitie_sortata)):
    print(propozitie_sortata[i])
