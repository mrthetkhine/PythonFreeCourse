#scenario 1
def inc(num):
    print("Inc ",num)
    num += 1
i = 100
inc(i)
inc(i)

print("i is ",i)

#scenario 2
def append(lst):
    lst.append(100)

my_list = []
append(my_list)
append(my_list)

print(" my_list After ",my_list)

#scenario 3
def update(lst):
    lst = [200,200]

update(my_list)
print(" my_list After ",my_list)