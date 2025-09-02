a=int(input("Enter a positive integer: "))
sign=-1 if a<0 else 1
a=abs(a)
reverse_num=0
while a>0:
    digit=a%10
    reverse_num=reverse_num*10+digit
    a//=10
reverse_num*=sign
print("Reversed integer: ",reverse_num)