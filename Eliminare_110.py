cuvant = input()
print(cuvant[1:])
for i in range(0, len(cuvant) - 2):
    print(cuvant[0:i + 1] + cuvant[i + 2:len(cuvant)+1])
print(cuvant[0:len(cuvant) - 1])