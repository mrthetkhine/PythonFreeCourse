class Student:
    def __init__(self,name,age):
        self._name = name
        self._age = age
        
    def set_age(self,age):
        if 0 > age>100:
            self._age = age
    
    def get_age(self):
        return self._age
    
    def display(self):
        print("Name ",self._name, " Age ",self._age)

mgMg = Student("Mg Mg",18)
#mgMg.name = "Name Change from outside"
mgMg.set_age(2000)
mgMg.display()
print("Read age ",mgMg.get_age())