lst = [10,20,30,40,50,10]
print("Length ",len(lst))
print("count 10 ",lst.count(10))
print("index 10 ",lst.index(10))
#print("find 100 ",lst.find(100))

lst.append(100)
print("after append ",lst)

lst2 = list(range(0,5))
print("list 2 ",lst2)
print("Sum ",sum(lst2))

lst2.insert(1,300)
print("list 2 ",lst2)

lst2.insert(-1,400)
print("list 2 ",lst2)