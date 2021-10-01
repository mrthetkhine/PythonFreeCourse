class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name ",self.name)
        print("Age ",self.age)

h1 = Human("Tk",37)
h1.school = "UCSY"
print("h1 ",h1.__dict__)