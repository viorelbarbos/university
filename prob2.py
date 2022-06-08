def CifraMaxima(x):
    maxi = 0
    while x != 0:
        if maxi <= x % 10:
            maxi = x % 10
            x = x / 10
        else:
            x = x / 10
    return maxi
if __name__ == "__main__":
    x = int(input())
    print(CifraMaxima(x))
