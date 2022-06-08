""" Calculul sumei S=1!+2!+...+n! utilizand o functie Python pentru
calculul factorialului."""


def fact(contor):
    F = 1
    for i in range(1, contor + 1):
        F *= i
    return F


S = 0
n = int(input("n= "))
for k in range(1, n + 1):
    S += fact(k)
print("suma factoriala = ", S)
