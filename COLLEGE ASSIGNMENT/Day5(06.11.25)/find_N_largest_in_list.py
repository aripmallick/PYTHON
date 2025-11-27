num=[23,12,30,45,67,89,34,22]
n=2
largest_numbers=sorted(set(num), reverse=True)[:n]
print(f"The {n} largest numbers in the list are:", largest_numbers)