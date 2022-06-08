
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # alfabetul englezesc
text = input("Introduceti textul pentru criptare:")  # citim textul pe care dorim sa-l criptam
cuvat_cheie = input("Introduceti cuvantul cheie:")  # citim cuvantul cheie pe care il adaugam la alfabet
cheie_deplasare = int(input("Introduceti cifra de deplasare:"))  # citim cheia de deplasare
cuvat_cheie = cuvat_cheie.upper()
text = text.upper()
for i in range(len(cuvat_cheie)):
    alfabet = alfabet.replace(cuvat_cheie[i], '')  # eliminam literele din alfabet care se regasesc in cuvatul cheie, deoarece nu trebuie sa fie dubluri
alfabet = cuvat_cheie + alfabet  # le concatenam
alfabet_nou = alfabet[len(alfabet) - cheie_deplasare:]  # realizam noul alfabet cu ajutorul cheii de deplasare
alfabet_nou = alfabet_nou + alfabet[:len(alfabet) - cheie_deplasare]
text_nou = list(text)
print(alfabet)  # afisam alfabetele ca sa vedem mai bine schimbarile
print(alfabet_nou)
for i in range(len(text)):  # criptam textul
    for j in range(len(alfabet)):
        if text[i] == alfabet[j]:
            text_nou[i] = alfabet_nou[j]
            break

print("".join(text_nou))  # afisam textul
