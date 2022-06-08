def ex_992(sir, caracter):  # definim o functie care verifica de cate ori un caracter apare intr-un cuvant
    aparitii = 0
    for i in range(len(sir)):
        if sir[i] == caracter:
            aparitii += 1
    return aparitii


if __name__ == '__main__':
    string = input()  # citim cuvantul
    vocale = "aeiouAEIOU"  # initializam un string care contile vocale
    nr_apvoc = 0
    for i in range(len(vocale)):  # patrcurgem stringul vocale
        nr_apvoc += ex_992(string,
                           vocale[i])  # numaram de cate ori o vocala apare in cuvantul citit prin apelarea functiei
    print(nr_apvoc)
