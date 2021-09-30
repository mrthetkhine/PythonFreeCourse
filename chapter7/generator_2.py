for i in range(0,5):
    print("I is",i)
    
def custom_range(start,end):
    for i in range(start,end+1):
        yield i

for i in custom_range(0,4):
    print("Custom range ",i)
    
def decend_to(num):
    while num >=0:
        yield num
        num = num -1

for i in decend_to(5):
    print("i descend ",i)