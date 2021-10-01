def push(lst,ele):
    lst.append(ele)

def pop(lst):
    if len(lst)>0:
        return lst.pop()
    else:
        return None
    
def is_empty(lst):
    return len(lst)==0
    
my_stack = []
push(my_stack,100)
push(my_stack,200)
push(my_stack,300)

while not is_empty(my_stack):
    print("Pop ",pop(my_stack))

print("is empty ",is_empty(my_stack))

another_list = ["Hello"]
push(another_list,100)