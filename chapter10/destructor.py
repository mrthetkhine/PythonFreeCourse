class MyClass:
    def __init__(self):
        self.list = [x for x in range(100000)]
    def __del__(self):
        print("Destructor ")
        self.list = None

a = MyClass()
del a