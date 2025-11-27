#USING LIST COMPREHENSION

num=[1,2,3,4,5,1,2,3,4,5]
element_to_delete=3 
new_num=[n for n in num if n!=element_to_delete]
print("Original List:",num)
print("List after deleting element",element_to_delete,":",new_num)

#USING REMOVE() FUNCTION

num=[4,24,5,10,20]
element_to_delete=5
print("Original List:",num)
while element_to_delete in num:
    num.remove(element_to_delete)
print("List after deleting element",element_to_delete,":",num)

#USING DEL STATEMENT

num=[7,14,21,28,35]
element_at_index=2
print("Original List:",num)
del num[element_at_index]
print("List after deleting element at index",element_at_index,":",num)

#USING filter() FUNCTION

num=[100,200,300,400,500]
element_to_delete=400
print("Original List:",num)
new_num=list(filter(lambda x:x!=element_to_delete,num))
print("List after deleting element",element_to_delete,":",new_num)

