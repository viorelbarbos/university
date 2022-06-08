propozitie = input()  # citim propozitia
cuvant = ""  # variabila pentru a ajuta la stocarea pe rand, a cuvintelor
lista_cuvinte3 = []  # lista de cuvinte cu 3 caractere
for i in range(len(propozitie)):  # parcurgem propozitia
    if propozitie[i] != ' ':  # daca nu suntem pe caracterul  spatiu, adunam caracterul la cuvant
        cuvant += propozitie[i]
    else:  # daca suntem pe caracterul spatiu, am format cuvantul
        if len(cuvant) == 3:  # daca cuvantul contine 3 caractere
            lista_cuvinte3.append(cuvant)  # il memoram in lista de cuvinte
        cuvant = ""  # resetam variabila pentru urmatorul cuvant
for i in range(len(lista_cuvinte3)):  # parcurgem lista de cuvinte care contine 3 caractere
    propozitie = propozitie.replace(lista_cuvinte3[i],
                                    '*')  # inlocuim din propozitie, cuvintele cu 3 caractere, cu caracterul '*'
print(propozitie)  # afisam propozitia modificata
