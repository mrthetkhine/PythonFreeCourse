class A:
    def __init__(self):
        print("A Constructor ")
    def methodA(self):
        print("Method A in class A")
class B:
    def __init__(self):
        print("B Constructor ")
    def methodB(self):
        print("Method B")
    def methodA(self):
        print("Method A in class B")
class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("Constructor C")
    def method(self):
        B.methodA(self)
        super().methodB()
    def methodA(self):
        print("C Method A")
c = C()
c.method()
c.methodA()
print("C MRO ", C.mro())