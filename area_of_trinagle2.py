import math
a=float(input("Enter a number: "))
b=float(input("Enter a number: "))
c=float(input("Enter a number: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle: ",area)

