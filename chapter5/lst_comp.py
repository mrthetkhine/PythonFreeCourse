lst = list(range(1,11))
print("list ",lst)

lst_two = []
for item in lst:
    lst_two.append(item*2)
print("List ",lst_two)

lst_three = [x*2 for x in lst]
print("Lst three ",lst_three)