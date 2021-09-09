lst = [10,20,30,40,50,10]
lst_two = [100,200]

lst.extend(lst_two)
print("Lst ",lst)

lst.remove(10)
print("Lst ",lst)

#lst.remove(110)
print("Lst pop ",lst.pop())
print("Lst pop ",lst.pop())
print("Lst pop ",lst.pop(3))
print("list ",lst)