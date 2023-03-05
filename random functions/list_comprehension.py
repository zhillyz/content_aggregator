#simple example
list_comp = [x-2 for x in range(1,4)]
print(list_comp)

#conditional list comprehension
even_nums = [x for x in range(24) if x % 2 == 0]
print(even_nums)

#so list comprehension just requires you to say you want
#newlist=[x,y,z for x in a thing for y in a thing for z in a thing if some things]
a=10
b=2
c=6
new_list = [[x,y,z] for x in range(0,a) for y in range(0,a) for z in range(0,c)]
print(new_list)