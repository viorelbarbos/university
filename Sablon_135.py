cuvant1, cuvant2 = input().split()  # citim cele doua cuvinte
vocale = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')  # sir de vocale
for i in range(len(cuvant1)):  # parcurgem cele doua siruri, litera cu litera
    if (cuvant1[i] in vocale) and (cuvant2[i] in vocale):  # daca pe ambele pozitii sunt vocale
        print('*', end='')  # printam *
    elif (cuvant1[i] not in vocale) and (cuvant2[i] not in vocale):  # daca pe ambele pozitii sunt consoane
        print('#', end='')  # printam #
    else:  # daca pe ambele pozitii nu sunt nici doar vocale sau consoane atunci una este consoana iar cealalta vocala sau invers
        print('?', end='')  # printam ?
