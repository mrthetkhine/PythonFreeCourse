
def first():
    a = "First"
    print("First called")
    return second() + 30 #60

def second():
    b = "Second"
    print("Second called")
    return third() +20 #30

def third():
    c ="Third"
    print("Third was called")
    return 10
x = first() #60
print("x is ",x)