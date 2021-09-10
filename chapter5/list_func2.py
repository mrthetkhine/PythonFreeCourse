lst =[10,-2,40,100,12]
lst.reverse()
print ("Reverse ", lst)

lst.sort()
print ("lst ", lst)

lst.sort(reverse=True)
print ("lst ", lst)

lst_two = lst[:]
print(" Id ",id(lst))
print(" Id ",id(lst_two))
print("list two ",lst_two)