"""Afisarea primilor n termeni ai unui sir recurent cu media aritmetica."""


def medarit(n, a, b):
    if n == 0:
        return a
    else:
        if n == 1:
            return b
        else:
            return (medarit(n - 1, a, b) + medarit(n - 2, a, b)) / 2


if __name__ == '__main__':
    n = int(input())
    a = eval(input())
    b = eval(input())
    print("primi", n, "termeni sunt", end=" ")
    for k in range(n):
        print(medarit(k, a, b), end=" ")
