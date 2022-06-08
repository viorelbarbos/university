sir = input()  # citesc sirul
lista_sir = list(sir)  # transform sirul intr-o lista
sir = ""  # variabila sir devine un string gol
vocale = ('a', 'e', 'i', 'o', 'u')  # definesc un sir care contine vocale
for i in range(len(lista_sir)):  # parcurg lista c
    if lista_sir[i] in vocale:  # daca un element din lista este vocala
        lista_sir[i] = lista_sir[i].upper()  # respectivul element este inlocuit cu litera mare corespunzatoare
sir = sir.join(lista_sir)  # refac sirul, modificat
print(sir)  # printez sirul
