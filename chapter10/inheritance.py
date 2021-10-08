class Human:
    def __init__(self,name, age):
        print("Human constructor name ",name, " age ",age )
        self.name= name
        self.age= age
    def work(self):
        print("Human ",self.name," work ")
    def eat(self):
        print("Human ",self.name," eat ")

class Doctor(Human):
    def __init__(self,name,age,medical_field):
        super().__init__(name,age)
        self.medical_field = medical_field
        print("Doctor consturctor ")
    
    def work(self):
        super().work();
        print("Doctor treat patient")

class Robot:
    def __init__(self):
        pass
    def work(self):
        print("Robot works") 

d = Doctor("Tin Shwe",40,"Heart")
d.work()
#d.eat()
d = Robot()
d.work()