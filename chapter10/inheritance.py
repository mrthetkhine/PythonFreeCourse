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

drTinShwe = Doctor("Tin Shwe",40,"Heart")
drTinShwe.work()
drTinShwe.eat()
