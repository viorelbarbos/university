from functii_utile import *


def ex_97(cuvant1, cuvant2):
    if len(cuvant1) != len(cuvant2):
        return 0
    lista_cuvant1 = string_to_list_character_wise(cuvant1)
    lista_cuvant2 = string_to_list_character_wise(cuvant2)
    lista_cuvant1.sort()
    lista_cuvant2.sort()
    print(lista_cuvant1, lista_cuvant1)
    if lista_cuvant1 == lista_cuvant2:
        return 1


if __name__ == '__main__':
    cuv1 = "rutina"
    cuv2 = "unitar"
    print(ex_97(cuv1, cuv2))
