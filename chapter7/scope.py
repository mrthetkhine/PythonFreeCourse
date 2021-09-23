x = "Hello"

def hello():
    y = "Inner Y"
    #x = "Change something" # x is no local
    global x #now x refered to global
    x = "Update global"
    print("X inside hello is ",x)
    print("Y inside hello ",y)
hello()

print("X outside ",x)
#print("Y outside ",y)