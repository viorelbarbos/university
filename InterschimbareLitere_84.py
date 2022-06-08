cuvant = input()  # citim cuvantul
vocale = ('a', 'e', 'i', 'o', 'u')  # initializam un string care contine vocale
poz_voc = 0  # variabila pentru a memora pozitia primei vocale
poz_cons = 0  # variabila pentru a memora pozitia ultimei consoane
for i in range(len(cuvant)):  # parcurgem cuvantul
    if cuvant[i] in vocale:  # cand gasim prima vocala ne oprim
        poz_voc = i
        break
for i in range(len(cuvant) - 1, 0, -1):  # parcurem cuvantul din spate, cand gasim consoana ne oprim
    if cuvant[i] not in vocale:
        poz_cons = i
        break
if poz_cons == 0:  # in cazul in care nu am gasit consoane, cuvantul este format doar din vocale, deci ne oprim
    print("IMPOSIBIL")
else:  # interschimbam prima vocala cu ultima consoana
    c = cuvant[poz_cons]
    v = cuvant[poz_voc]
    cuvant = cuvant.replace(cuvant[poz_cons], v, 1)
    cuvant = cuvant.replace(cuvant[poz_voc], c, 1)
    print(cuvant)
