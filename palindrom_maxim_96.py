def palindrom(cuvant):
    if cuvant.lower() == cuvant[::-1].lower():
        return True
    return False


propozitie = input()
lista_propozitie = propozitie.split(' ')
pozitie = 0
lungime_maxima = 0
for i in range(len(lista_propozitie)):
    if palindrom(lista_propozitie[i]):
        lungime_variabila = len(lista_propozitie[i])
        if lungime_maxima < lungime_variabila:
            lungime_maxima = lungime_variabila
            pozitie = i
print(lista_propozitie[pozitie])
