num=int(input("Enter a number: "))
temp=num
reverse_num=0
while num>0:
    digit=num%10
    reverse_num=reverse_num*10+digit
    num//=10
if temp==reverse_num:
    print(f"{temp} is a plalindrome number")
else:
    print(f"{temp} is not a palindrome number")