from math import tan
n=int(input("Input number of sides: ")); a=int(input("Input the lenght of a sides: "))
rad=(180/n)*(3.141/180)
apo=a/(2*(tan(rad)))
print("The area of the polygon is: "+str(int(n*(apo*(a/2)))))