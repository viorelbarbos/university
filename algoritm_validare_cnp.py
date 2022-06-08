i = 0
CNP = []
for i in range(0, 13):
    x = int(input("Adauati cifra CNP:"))
    CNP.append(x)
i = 0
SC = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
S = 0
for i in range(0, 12):
    S = S + CNP[i] * SC[i]
R = S % 11
if R == 10:
    CC = 1
else:
    CC = R 
if CC == CNP[12]:
    print("CNP CORECT")
else:
    print("CNP INCORECT")
