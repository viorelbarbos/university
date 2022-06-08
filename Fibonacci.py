"""Afisarea primilor n termeni ai unui sir Fibonacci."""


def fibonaccirec(n, a, b):
    if n == 0:
        return a
    else:
        if n == 1:
            return b
        else:
            return fibonaccirec(n - 1, a, b) + fibonaccirec(n - 2, a, b)


if __name__ == '__main__':
    n = int(input())
    a = eval(input())
    b = eval(input())
    for k in range(n):
        print(fibonaccirec(k, a, b), end=" ")
