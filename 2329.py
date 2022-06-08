def ex_2329(n,v):
    nr = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            ok = 0
            s = 0
            s = v[i] + v[j]
            if s == 2:
                ok = 1
            else:
                for divizor in range(2, s):
                    if s % divizor == 0:
                        ok = 1
                        break
            if ok != 1:
                nr +=1
    print(nr)

if __name__ == "__main__":
    v = [2, 5, 9]
    n = 3
    ex_2329(n, v)