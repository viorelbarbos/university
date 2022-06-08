n = int(input("n="))
XSS = []
YSS = []
XDJ = []
YDJ = []
for i in range(0, n):
    print('XSS[', i, ']= ', )
    XSS.append(eval(input()))
    print('YSS[', i, ']= ', )
    YSS.append(eval(input()))
    print('XDJ[', i, ']= ', )
    XDJ.append(eval(input()))
    print('YDJ[', i, ']= ', )
    YDJ.append(eval(input()))
Xstanga = XSS[0]
Xdreapta = XDJ[0]
Yjos = YDJ[0]
Ysus = YSS[0]
for i in range(1, n):
    if Xstanga < XSS[i]:
        Xstanga = XSS[i]
    if Xdreapta > XDJ[i]:
        Xdreapta = XDJ[i]
    if Yjos < YDJ[i]:
        Yjos = YDJ[i]
    if Ysus > YSS[i]:
        Ysus = YSS[i]
if (Xdreapta < Xstanga) or (Ysus < Yjos):
    print("Intersectia este vida")
else:
    Aria = (Xdreapta - Xstanga) * (Ysus - Yjos)
    print("Aria intersectiei este ", format(Aria, '.2f'))
