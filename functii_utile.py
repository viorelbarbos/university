def string_to_list(string):
    lista = list(string.split(" "))
    return lista


def string_to_list_character_wise(string):
    return list(string)


def prim(p):
    nr_prim = True
    if p == 1 or p == 0:
        nr_prim = False
        return nr_prim
    for contor in range(2, p // 2):
        if p % contor == 0:
            nr_prim = False
    return nr_prim
