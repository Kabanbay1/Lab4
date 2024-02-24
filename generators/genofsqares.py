def sqares(a,b):
    if a!=b+1:
        yield a*a
a=int(input("1: "))
b=int(input("2: "))
for i in range((b+1)-a):
    x=sqares(a+i,b)
    print(next(x))