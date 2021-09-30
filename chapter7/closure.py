def counter():
    print("Counter Func")
    i = 1
    def next():
        nonlocal i 
        i = i + 1
        #print("Inner func ",i)
        return i
    return next
    
next_func = counter()
print("Next ",next_func())
print("Next ",next_func())