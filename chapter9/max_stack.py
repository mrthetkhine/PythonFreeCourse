def push(lst,max,ele):
    if(len(lst)<max):
        lst.append(ele)
    else:
        print("Error")

def pop(lst):
    if len(lst)>0:
        return lst.pop()
    else:
        return None
    
def is_empty(lst):
    return len(lst)==0
    
max_legth = 5
my_stack = []

push(my_stack,max_legth,100)
push(my_stack,max_legth,200)
push(my_stack,max_legth,300)
push(my_stack,max_legth,200)
push(my_stack,4,300)
push(my_stack,max_legth,300)

while not is_empty(my_stack):
    print("Pop ",pop(my_stack))

print("is empty ",is_empty(my_stack))

another_list = ["Hello"]
push(another_list,max_legth,100)