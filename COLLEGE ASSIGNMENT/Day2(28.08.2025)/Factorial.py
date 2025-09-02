num=int(input("Enter the number: "))
fact=1
if num < 0:
    print("Factorial does not exist negative number")
elif num == 0:
    print("Factorial of is 1")
else:
    for i in range (1,num+1):
        fact=fact*i
    print(f"Factorial of {num} is: {fact}")