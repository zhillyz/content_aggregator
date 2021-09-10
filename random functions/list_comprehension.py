#simple example
list_comp = [x-2 for x in range(1,4)]
print(list_comp)

#conditional list comprehension
even_nums = [x for x in range(24) if x % 2 == 0]
print(even_nums)
