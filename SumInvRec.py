"""Calculul sumei inverselor primelor n numere naturale
cu ajutorul functiei recursive."""


def sumrecinv(n):
    if n == 1:
        return 1
    else:
        return 1 / n + sumrecinv(n - 1)

if __name__ == '__main__':
    n = int(input("n="))
    print("suma inverselor primelor", n, "numere naturale este ", sumrecinv(n))
