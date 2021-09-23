from functools import *
my_lst = [1,2,3,4,5]
#add = lambda x,y : x +y

def add(a,b):
    print("A ",a, " b ", b)
    return a+b
sum = reduce(add,my_lst)
print("Sum is ",sum)