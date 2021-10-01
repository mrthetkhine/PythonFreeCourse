#st(lst,max_length)
def push(st,ele):
    if(len(st[0])<st[1]):
        st[0].append(ele)
    else:
        print("Error")

def pop(st):
    if len(st[0])>0:
        return st[0].pop()
    else:
        return None
    
def is_empty(st):
    return len(st[0])==0
    
max_legth = 5
my_stack = []
st = (my_stack,max_legth)

push(st,100)
push(st,200)
push(st,300)
push(st,200)
push(st,300)
push(st,300)

while not is_empty(st):
    print("Pop ",pop(st))

print("is empty ",is_empty(st))

