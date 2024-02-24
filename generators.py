#1 Create a generator that generates the squares of numbers up to some number N.
def Sqrgen(N): 
    a=1
    while a!=N:
        yield a*a
        a+=1
N=int(input("Limit of Squaring: "))
x=Sqrgen(N)
for i in range (N-1):
    print(next(x))
#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
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
#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
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
#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def sqares(a,b):
    if a!=b+1:
        yield a*a
a=int(input("1: "))
b=int(input("2: "))
for i in range((b+1)-a):
    x=sqares(a+i,b)
    print(next(x))
#5 Implement a generator that returns all numbers from (n) down to 0.
def fromntozero(n):
    while n>0:
        n-=1
        yield n
n=int(input("Number: "))
x=fromntozero(n+1)
for i in range(n+1):
    print(next(x))