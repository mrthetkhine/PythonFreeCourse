class Money:
    def __init__(self,value):
        self.value = value
    def __radd__(self,other):
        print("R Add called")
        return Money(self.value+other)
    def __add__(self,other):
        print("Add called")
        return Money(self.value+other.value)
    def __iadd__(self,other):
        print("I add called")
        return Money(self.value+other.value)
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self,other):
        return self.value< other.value
    def __repr__(self):
        return "(Money {})".format(self.value)
    def __str__(self):
        print("Called str")
        return "(Money {})".format(self.value)

m1 = Money(10)
m2 = Money(20)
m3 = m1 + m2 + Money(20)
print("M3 ",m3 == Money(50))
print("M3 < 60 ", m3 < Money(60))
m3 += Money(10)
print("M3 ",m3)
print("M3 ", str(m3) + " is ")
print("M4 ", 20+ Money(10))