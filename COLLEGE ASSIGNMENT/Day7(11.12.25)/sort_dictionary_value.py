#Ascending order
d={'a':30,'b':10,'c':15,'d':20}
sorted_dict_asc=dict(sorted(d.items(),key=lambda item:item[1]))
print("Dictionary sorted in ascending order by value:",sorted_dict_asc)

#Descending order
d={'a':30,'b':10,'c':15,'d':20}
sorted_dict_desc=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
print("Dictionary sorted in descending order by value:",sorted_dict_desc)