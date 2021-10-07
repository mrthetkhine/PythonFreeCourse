class Human:
    planet = "Earth" #static variable
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name ",self.name , " Age ",self.age,  "Planet ", Human.planet)
    def changePlanet(self,newPlanet):
        self.planet = newPlanet
    @classmethod
    def class_method(cls):
        print("Class method >>",cls.planet)
    @staticmethod
    def static_method():
        print("Normal static method ",Human.planet)

h1 = Human("Tk",37)
h1.school = "UCSY"
del h1.school
print("h1 ",h1.__dict__)
h1.display()

h2 = Human("Mg Mg",18)
h2.display()

Human.planet = "Mars"
h1.display()
print()
h2.display()

h1.class_method()
Human.class_method()

h1.static_method()
Human.static_method()