def sterge_42(vector, nr_elemente, i, j):
    for contor in range(i, j):
        del(vector[contor])
    print(vector)

if __name__ == '__main__':
    nr_elemente = int(input())
    vector = []
    for k in range(0, nr_elemente):
        aux = int(input())
        vector.append(aux)
    i = int(input())
    j = int(input())
    sterge_42(vector, nr_elemente, i, j)
