def Sqrgen(N): 
    a=1
    while a!=N:
        yield a*a
        a+=1
N=int(input("Limit of Squaring: "))
x=Sqrgen(N)
for i in range (N-1):
    print(next(x))