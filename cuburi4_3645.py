"""Ştiind că un turn poate fi format din cel puţin un cub, scrieţi un program care să determine:
1. cel mai mare număr de cuburi alăturate care au laturile exprimate printr-un număr par de centimetri;
2. înălţimea (exprimată în centimetri) celui mai înalt turn construit de robot."""

"""De la tastatură se citesc două numere natural C și N, în această ordine.
 C reprezintă numărul cerinţei şi poate avea două valori 1 sau 2 iar N reprezintă numărul cuburilor de pe masa de lucru.
 Se citesc apoi N numere naturale ce reprezintă lungimile laturilor cuburilor, în ordinea numerotării acestora."""
C = int(input())
N = int(input())
if C == 1:
    lungime_maxima = 0
    lungime_temporala = 0
    for i in range(N):
        numar = int(input())
        if numar % 2 == 0:
            lungime_temporala += 1
        else:
            if lungime_maxima < lungime_temporala:
                lungime_maxima = lungime_temporala
            lungime_temporala = 0
    print(lungime_maxima)
else:
    stiva_maxima = 0
    stiva_temporala = int(input())
    auxiliar_numar = stiva_temporala
    for j in range(N-1):
        numar = int(input())
        if auxiliar_numar > numar:
            stiva_temporala += numar
            auxiliar_numar = numar
        else:
            if stiva_maxima < stiva_temporala:
                stiva_maxima = stiva_temporala
                stiva_temporala = numar
                auxiliar_numar = numar
    print(stiva_maxima)
