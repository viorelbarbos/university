n = int(input())
# n=5 -->1, 5
maxim = 0
for i in range(0, n):
    x = int(input())
    if maxim < x:
        maxim = x
print(maxim)
