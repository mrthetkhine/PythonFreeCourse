a = 10
b = a

a += 1
print("B ",b)
print("a ",a)

lst = [100,200]
lst_two = lst

lst.append(300)
lst_two.append(400)

print("lst ",lst , "id ",id(lst))
print("Lst_two ",lst_two, " id ", id(lst_two))

lst_two = [400,500]
lst_two.append(100)

print("lst ",lst , "id ",id(lst))
print("Lst_two ",lst_two, " id ", id(lst_two))