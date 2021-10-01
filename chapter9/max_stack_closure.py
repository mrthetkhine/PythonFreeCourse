def stack(max_legth):
    lst = []
    def push(ele):
        #print("push ")
        if(len(lst)< max_legth):
            lst.append(ele)
            
    def pop():
        #print("Pop ")
        if not is_empty():
            return lst.pop()
        else:
            return None
        
    def is_empty():
        #print("is empty")
        return len(lst) ==0 
    return (push,pop,is_empty)
    
push,pop,is_empty = stack(5)

push(10)
push(20)
push(30)
push(10)
push(20)
push(30)

print("pop ",pop())
print("pop ",pop())
print("pop ",pop())
print("pop ",pop())

st1_push,st1_pop,st1_is_empty = stack(5)