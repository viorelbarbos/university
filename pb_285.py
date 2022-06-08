"""Se dă un număr natural, k.
 Să se determine toate perechile de numere naturale nenule x, y (x<=y), cu proprietatea că x2+y2=k ."""

k = int(input())
for x in range(2, k // 10):
    for y in range(x, k // 10):
        if x**2 + y**2 == k:
            print(x, y)
