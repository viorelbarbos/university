"""Afisarea primilor n termeni ai unui sir recurent cu media armonica."""


def medarmonica(n, a, b):
    if n == 0:
        return a
    else:
        if n == 1:
            return b
        else:
            return 2*medarmonica(n - 1, a, b) * medarmonica(n - 2, a, b) / (medarmonica(n - 1, a, b) + medarmonica(n - 2, a, b))


if __name__ == '__main__':
    n = int(input())
    a = eval(input())
    b = eval(input())
    print("primi", n, "termeni sunt", end=" ")
    for k in range(n):
        print(medarmonica(k, a, b), end=" ")
