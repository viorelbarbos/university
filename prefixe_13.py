sir = input("sir=")
ok = True
while ok:
    if len(sir) > 10:
        print("Ati adaugat un cuvant cu prea multe litere!")
        print("sir=");sir = input()
    else:
        break
for i in range(len(sir)):
    print(sir[0:len(sir) - i])
for i in range(len(sir)):
    print(sir[i::])
