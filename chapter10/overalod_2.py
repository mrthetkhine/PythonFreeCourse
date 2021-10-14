def method(): 
    print("Version 1")
def method(a):
    print("Version 2")
def method(a,b): #overwrite
    print("Version 3")
    
method(1,2)
