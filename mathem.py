from math import *
#1 Write a Python program to convert degree to radian.
x=int(input("Input degree: "))
print("Output radian: "+str(x*(pi/180)))
#2 Write a Python program to calculate the area of a trapezoid.
x=int(input("Height: "))
y=int(input("Base, first value: ")); z=int(input("Base, second value: "))
print("Expected Output: "+str(((y+z)/2)*x))
#3 Write a Python program to calculate the area of regular polygon.
n=int(input("Input number of sides: ")); a=int(input("Input the lenght of a sides: "))
rad=(180/n)*(3.141/180)
apo=a/(2*(tan(rad)))
print("The area of the polygon is: "+str(int(n*(apo*(a/2)))))
#4 Write a Python program to calculate the area of a parallelogram.
a=float(input("Length of base: ")); h=float(input("Height of parallelogram: "))
print("Expected Output: "+str(a*h))

