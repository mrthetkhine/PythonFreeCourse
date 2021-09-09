lst = [10,20,30,40,50]
lst[0] = 20
print("list ",lst, " type ",type(lst))

lst_1_to_ten = list(range(1,10,2))
print("list from range ",lst_1_to_ten)

str_list = "Hello World".split()
str_list[0] = str_list[0].upper()
print("Str_list ",str_list)

my_str = "hello"
#my_str[0] = "K"
my_str = "How are you"
print("str [0] ",my_str[0])

for i in lst:
    i = i+1
    print("Item => ",i)

for index,value in enumerate(lst):
    lst[index] *= 2
print("Double list ",lst)