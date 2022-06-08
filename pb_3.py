alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabet = list(alfabet)
text = input("Introduceti textul pentru a fi criptat")
print("Introduceti cele doua chei")
a = int(input())
b = int(input())
i = 0
text1 = list(text)
while i < len(text):
    if text1[i] != ' ':
        j = alfabet.index(text1[i])
        d = (a * j + b) % 26
        text1[i] = alfabet[d]
        i += 1
    else:
        i += 1


print("".join(text1))
