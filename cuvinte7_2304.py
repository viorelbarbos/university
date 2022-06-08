n = int(input())  # citim numarul n care reptezinta numarul de cuvinte care urmeaza a fi citite
lista_cuvinte = []  # initializam o lista vida pentru cuvinte
for i in range(n):
    lista_cuvinte.append(input())  # citim cuvintele
lungime_cuvant = int(input())  # citim un numar, care reprezita lungimea cuvintelor care vor fi afisate primele
lista_noua = []  # initializam o lista unde vom stoca cuvintele care au lungimea 'lungime_cuvat' primele apoi restul
for i in range(n):
    if len(lista_cuvinte[i]) == lungime_cuvant:  # adaugam noii liste cuvintele care au lungimea ceruta
        lista_noua.append(lista_cuvinte[i])
for i in range(n):
    if len(lista_cuvinte[i]) != lungime_cuvant:  # adaugam restul cuvintelor
        lista_noua.append(lista_cuvinte[i])
for i in range(n):  # afisam noua lista care respecta cerinta data
    print(lista_noua[i], end=' ')
