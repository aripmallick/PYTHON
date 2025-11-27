#USING SET() FUNCTION

num=[1,2,3,4,5,1,2,3,4,5]
print("Original List:",num)
new_num=list(set(num)) 
print("List after removing duplicates:",new_num)

#USING FOR LOOP

num=[1,2,3,4,5,1,2,3,4,5]
new_num=[]
for n in num:
    if n not in new_num:
        new_num.append(n)
print("Original List:",num)
print("List after removing duplicates:",new_num)

#USING FROMKEYS() FUNCTION

num=[1,2,3,4,5,1,2,3,4,5]
new_num=list(dict.fromkeys(num))
print("Original List:",num)
print("List after removing duplicates:",new_num)