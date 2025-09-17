a = int(input("Enter the lower number: "))
b = int(input("Enter the upper number: "))

print(f"All Prime numbers are of this({a},{b}) interval: ")

for i in range(a,b+1):
    if i<=1:
        print("Interval is not valid")
        break
    is_prime = 1
    for j in range(2, int(i**0.5) + 1):  # check up to √num
        if i % j == 0:
            is_prime = 0
            break

    if is_prime:
        print(i)