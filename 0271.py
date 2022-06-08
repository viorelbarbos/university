def ex_0271(n, v):
    numar = 0
    for i in range(0, n):
        for j in range(0, n - 1):
            for k in range(j, n - 1):
                if i != j and j != k and i != k and v[i] == v[j] + v[k]:
                    print(v[i], v[j], v[k], end=" ")
                    numar += 1
    print(numar)


if __name__ == "__main__":
    v = [1, 10,25 ,6,2,15,3]
    n = 7
    print(ex_0271(n, v))
