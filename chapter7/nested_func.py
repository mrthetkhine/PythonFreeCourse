def outer_func():
    print("Outer Func")
    i = 1
    def inner():
        print("Inner func ",i)
    inner()
    
outer_func()