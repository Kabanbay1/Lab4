def fromntozero(n):
    while n>0:
        n-=1
        yield n
n=int(input("Number: "))
x=fromntozero(n+1)
for i in range(n+1):
    print(next(x))