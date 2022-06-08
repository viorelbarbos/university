n = int(input())
f1 = 1
f2 = 1
if n == 1:
    print(f1)
else:
    print(f1, f2, end = " ")
for i in range(3, n+1):
    s = f1 + f2
    print(s, end = " ")
    f1 = f2
    f2 = s