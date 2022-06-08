"""Inlocuire termeni sir numere cu media aritmetica a celorlalte."""
n = int(input("n="))
a = []
for i in range(0, n):
    print("Introduceti a[", i, "]=")
    a.append(eval(input()))
print("Sirul dat este : ", a)
S = 0
for i in range(0, n):
    S = S + a[i]
for i in range(0, n):
    a[i] =(S - a[i]) / (n - 1)
print("Sirul modificat este : ", a)
