def sterge_42(vector, nr_elemente, i, j):
    for contor in range(i, j):
        del(vector[contor])
    print(vector)

if __name__ == '__main__':
    nr_elemente = int(input())
    i = int(input())
    j = int(input())
    vector = []
    for k in range(0, nr_elemente):
        aux = int(input())
        vector.append(aux)
    sterge_42(vector, nr_elemente, i, j)
    #n = 6
    #x = [12, 7, 6, 3, 8, 5]
    #i = 2
    #j = 4
    #sterge_42(x, n, i, j)