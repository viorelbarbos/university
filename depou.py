stiva_a = []
stiva_b = []
n = int(input())
for i in range(1, n + 1):
    aux = int(input())
    stiva_a.append(aux)
contor = 1
rezultat = []
p = 1
while stiva_a or stiva_b:
    if stiva_b and stiva_b[-1] == contor:
        stiva_b.pop()
        contor += 1
        rezultat.insert(p + 1, 2)
        rezultat.insert(p + 2, 3)
        p += 2
    else:
        while stiva_a and stiva_a[-1] != contor:
            if stiva_b and stiva_a[-1] >= stiva_b[-1]:
                break
            stiva_b.append(stiva_a[-1])
            stiva_a.pop()
            rezultat.insert(p + 1, 1)
            rezultat.insert(p + 2, 2)
            p += 2
        if stiva_a[-1] != contor:
            break
        else:
            rezultat.insert(p + 1, 1)
            rezultat.insert(p + 2, 3)
            p += 2
            stiva_a.pop()
            contor += 1
if contor < n:
    print(0)
else:
    print(int((p - 1) / 2))
    print("\n")
    for i in range(len(rezultat)):
        if rezultat[i] == 1:
            print("A ")
        if rezultat[i] == 2:
            print("B ")
        if rezultat[i] == 3:
            print("C ")
        if i % 2 == 1:
            print("\n")