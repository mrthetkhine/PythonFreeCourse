my_set = {1,2,3,5}
my_set.add(100)
my_set.update([-10,20,30],range(5))
print("MySet ",my_set)

set_clone = my_set.copy()
print("MySet is set_clone ",my_set is set_clone)

print("set_clone ",set_clone)
element = 10
#element in set_clone and set_clone.remove(element)
set_clone.discard(element)

set_clone.clear()
while len(set_clone)>0:
    print("Pop ",set_clone.pop())

print("Union ", {1,2} | {3,4,1}, " ",{1,2}.union({3,4,1}))
print("Intersect ", {1,2} & {3,4,1}, " ",{1,2}.intersection({3,4,1}))
print("Diff ", {1,2} - {3,4,1}, " ",{1,2}.difference({3,4,1}))
print("System Diff ", {1,2} ^ {3,4,1}, " ",{1,2}.symmetric_difference({3,4,1}))