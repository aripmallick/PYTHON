num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

if sum == temp:
    print(temp, "is an Armstrong Number")
else:
    print(temp, "is NOT an Armstrong Number")



#Example: 153 = 1³ + 5³ + 3³ if calculate value is same then it is called armstrong number