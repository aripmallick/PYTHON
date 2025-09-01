a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

d=(a & b)
e=(a | b)
f=(~a)
leftShift=(a << b)
rightShift=(a >> b)
print("And operation: ",d)
print("OR operation: ",e)
print("NOt operation: ",f)
print("Left shift operation: ",leftShift)
print("Right shift operation: ",rightShift)

