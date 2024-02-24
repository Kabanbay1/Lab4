def div_by(n):
    a=0
    for i in range(n+1):
        if a%3==0 and a%4==0:
            yield a
        a+=1
n=int(input("Limit of numbers: "))
x=div_by(n)
for j in range(int(n/12)+1):
    print(next(x))