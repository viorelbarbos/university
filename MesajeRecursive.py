"""Afisarea de n ori a unui mesaj prin procedeu recursiv."""


def nprint(mesaj, n):
    if n >= 1:
        print(mesaj, end=" ")
        nprint(mesaj, n - 1)


if __name__ == '__main__':
    nprint("ana", 3)
