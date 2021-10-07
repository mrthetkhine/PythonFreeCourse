class LookupDemo:
    planet="Earth"
    def __init__(self):
        pass
    def display(self):
        print("self.planet ",self.planet)
    def changePlanet(self,newPlanet):
        self.planet = newPlanet
        name = newPlanet

l1 = LookupDemo()
l1.display()
print("l1 instance ", l1.__dict__)
l1.changePlanet("Mars")
l1.display()
print("l1 instance ", l1.__dict__)
l2 = LookupDemo()
l2.display()

#del l2.planet
del LookupDemo.planet