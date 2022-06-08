propozitie = input()  # citim propozitia
propozitie += ' '  # adaugam un spatiu la finalul propozitiei citite pentru a putea prelucra toate cuvintele
auxiliar_propozitie = ""  # initializam un sir gol pentru a fi prelucrat
cuvant = ""  # initializam un sir pentru a fi adaugate, pe rand, cuvintele
for i in range(len(propozitie)):  # parcurgem propozitia
    if propozitie[i] != ' ':  # daca nu suntem pe caracterul spatiu
        cuvant = cuvant + propozitie[i]  # adaugam litera la cuvant
    elif len(cuvant) > 0:  # daca am creat cuvantul
        auxiliar_propozitie += cuvant + ' '  # adaugam cuvantul la propozitia auxiliara urmata de un spatiu
        cuvant = ""  # stergem cuvantul creat inainte pentru a face loc altuia
auxiliar_propozitie = auxiliar_propozitie[:len(
    auxiliar_propozitie) - 1]  # din cauza ca la finalul propozitiei auxiliare se adauga un spatiu suplimentar trebuie sa-l stergem
print(auxiliar_propozitie)  # afisam propozitia fara spatiile inutile
