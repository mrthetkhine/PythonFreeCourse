def list_total(lst=[]):
    print("Lst ",lst)
    return sum(lst)

print("total ",list_total([1,2,3,4]))
print("total ",list_total())

def append(lst=[]):
    lst.append(100)
    return lst

my_lst = [1,2,3]
print("List append ",append(my_lst))

print("List append ",append())
print("List append ",append())