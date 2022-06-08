fisier = open("maxmat.in", "r")
matrice = []
prima_linie = fisier.readline().strip().split(' ')
n = int(prima_linie[0])
m = int(prima_linie[1])
print(prima_linie)
for linie in fisier.readlines():
    matrice.append([int(x) for x in linie.strip().split(' ')])
print(matrice)
fisier.close()
scriere_fisier = open("maxmat.out", "w")
for i in range(n):
    scriere_fisier.write(str(max(matrice[i])))
    scriere_fisier.write(' ')
    scriere_fisier.write(str(matrice[i].index(max(matrice[i])) + 1))
    scriere_fisier.write('\n')
scriere_fisier.close()
