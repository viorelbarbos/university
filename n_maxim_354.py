n = int(input())
maxim = 0
for i in range(0, n):
    x = int(input())
    if maxim < x:
        maxim = x
print(maxim)
