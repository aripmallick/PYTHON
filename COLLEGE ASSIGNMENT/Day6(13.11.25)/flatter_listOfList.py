#usiing list comprehension

num_of_lists=[[1,2,3],[4,5],[6,7,8,9]]
flat_list=[item for sublist in num_of_lists for item in sublist]    
print("Original List of Lists:",num_of_lists)
print("Flattened List:",flat_list)

#using itertools.chain()

import itertools
num_of_lists=[[10,20,30],[40,50],[60,70,80,90]]
flat_list=list(itertools.chain.from_iterable(num_of_lists))
print("Original List of Lists:",num_of_lists)
print("Flattened List:",flat_list)

#using sum() function
num_of_lists=[[100,200,300],[400,500],[600,700,800,900]]
flat_list=sum(num_of_lists,[])
print("Original List of Lists:",num_of_lists)
print("Flattened List:",flat_list)

#using numpy.flatten() library

import numpy as np
num_of_lists=[[11,22,33],[44,55,66],[77,88,99]]
flat_list=np.array(num_of_lists).flatten()
print("Original List of Lists:",num_of_lists)
print("Flattened List:",flat_list)

