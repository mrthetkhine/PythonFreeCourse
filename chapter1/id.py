x = 1500
y = int(1500)
print(" x is y ", x is y)

def hello():
    k = 1500
    print("id of k ",id(k))

hello()
print("Id of x ",id(x))
print("Id of y ",id(y))