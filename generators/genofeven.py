def generate_evens(n):
    a=0
    for i in range(n):
        if a%2==0:
            yield a
        a+=1

n=int(input("Limit of Evens: "))
x=generate_evens(n+10)
for j in range(int(1+n/2)):
    print(str(next(x)), end=",")