n = int(input())
ok = 0
if n > 2000000000:
    print(" ")
else:
     while n>0 and ok==0:
        if (n % 10) % 2 ==0:
             ok=1
             print(n % 10)
        else:
            n //=10
if ok == 0:
    print("-1")
