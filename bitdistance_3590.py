n = int(input())
n_baza2 = []
while n>0:
    n_baza2.append(n % 2)
    n //= 2
print(len(n_baza2) - 2)