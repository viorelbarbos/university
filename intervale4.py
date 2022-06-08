fisier = open('intervale4.in', 'r')  # deschidem fisierul
prima_linie = fisier.readline().strip().split(' ')  # citim prima linie, unde avem numarul de intervale
nr_intervale = int(prima_linie[0])
punct_x = []  # contine coordonatele de pe abscisa
punct_y = []  # contine coordonatele de pe ordonata

for i in range(nr_intervale):  # citim intervalele din fisier, le adaugam in doua stive
    linie = fisier.readline().strip().split(' ')
    punct_x.append(int(linie[0]))
    punct_y.append(int(linie[1]))

i = 0
while i < nr_intervale: # cat timp parcurgem intervalele
    while i >= 1 and not (punct_x[i] > punct_y[i - 1] or punct_y[i] < punct_x[i - 1]): # daca  i >= 1 si conditia negata este adevarata
        punct_x[i - 1] = min(punct_x[i], punct_x[i - 1])
        punct_y[i - 1] = max(punct_y[i], punct_y[i - 1])
        print("min", punct_x[i], punct_x[i - 1])
        print("max", punct_y[i], punct_y[i - 1])
        print(i)
        print(punct_x[i], ">", punct_y[i - 1], "or", punct_y[i], '<', punct_x[i - 1])
        for j in range(nr_intervale):
            print(punct_x[j], " ", punct_y[j])
        print("------")
        punct_x.pop(i)
        punct_y.pop(i)
        i -= 1
        nr_intervale -= 1
        for j in range(nr_intervale):
            print(punct_x[j], " ", punct_y[j])
        print("\n\n\n")
    i += 1

print("Intervalele ramase sunt: ")
for i in range(len(punct_x)):
    print(punct_x[i], " ", punct_y[i])
print("\nNumarul de intervale ramase: ")
print(nr_intervale, "\n")
