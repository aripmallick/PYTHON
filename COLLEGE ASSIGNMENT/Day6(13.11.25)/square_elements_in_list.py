#USING COMPREHENSING

num=[1,2,3,4,5]
squared_num=[n**2 for n in num]
print("Original List:",num)
print("List after squaring each element:",squared_num)

#USING LOOP

num=[4,3,2,1,5]
squares=[]
for n in num:
    squares.append(n**2)    
print("Original List:",num)
print("List after squaring each element:",squares)