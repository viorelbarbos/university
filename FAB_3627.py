"""Subprogramul returnează 1 dacă orice număr din vectorul b se poate scrie ca sumă a două numere aflate pe poziții
diferite în a, sau 0 în că există cel puțin un număr din b care nu se poate scrie ca sumă de două numere aflate pe
poziții diferite în a. """


def ex_3627(list1, nr_elemente_list1, list2, nr_elemente_list2):
    ok = 0
    k = 0
    for i in range(0, nr_elemente_list2):
        for j in range(0, nr_elemente_list1):
            for k in range(j + 1, nr_elemente_list1 - 1):
                if list1[j] + list1[k] == list2[i]:
                    k += 1
                    ok = 1
                    break
            if ok == 1:
                ok = 0
                break
    if k == nr_elemente_list2:
        return 1
    return 0


if __name__ == '__main__':
    a = [-1, 4, 3, 7]
    b = [2, 11, 7]
    n = 4
    m = 3
    print(ex_3627(a, n, b, m))
