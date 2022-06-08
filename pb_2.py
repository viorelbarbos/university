text = "SILENCE IS GOLD FOR ANDREI AND VIOREL"
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabet = list(alfabet)
matrice = [
    [9, 1],
    [21, 8]
]
while len(text)%2 != 0:
    text += 'Q'

text = text.replace(' ', 'Q')
i = 0
print(text)
text_criptat = []
while i < len(text) - 1:
    lista = []
    lista.append(alfabet.index(text[i]))
    lista.append(alfabet.index(text[i + 1]))
    i += 2
    cuvant = []
    for j in range(len(lista)):
        aux = 0
        for k in range(len(lista)):
            aux += lista[k] * matrice[k][j]
        cuvant.append(aux % 26)
    text_criptat.append(alfabet[cuvant[0]])
    text_criptat.append(alfabet[cuvant[1]])

print("".join(text_criptat))