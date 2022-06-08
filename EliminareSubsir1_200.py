propozitie = input() # citim propozitia
cuvant = input() # citim cuvantul
propozitie_inversa = propozitie[::-1] # memoram intr-o variabila propozitia scrisa invers, pentru a determina mai usor ultima aparitie
propozitie_inversa = propozitie_inversa.replace(cuvant[::-1], '', 1) # stergem prima aparitie a cuvantului din propozitie
propozitie = propozitie_inversa[::-1] # aducem propozitia la forma initiala scriind invers propozitia scrisa adineaori invers
print(propozitie) # afisam propozitia fara ultima aparitie a cuvantului
