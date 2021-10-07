class Student:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    @property  
    def age(self):
        print("getter called")
        return self._age 
    
    @age.setter
    def age(self,age):
        print("setter run")
        if 0 > age>100:
            self._age = age
    @age.deleter
    def age(self):
        print("Delete ")
        del self._age
        
    def display(self):
        print("Name ",self._name, " Age ",self._age)

class School:
    def __init__(self):
        self._student_list = []
    def enroll(self,student):
        print("Student ",student._name, " Have been enrolled")
        self._student_list.append(student)

mgMg = Student("Mg Mg",18)
#mgMg.name = "Name Change from outside"
print("Read age ",mgMg.age)
mgMg.age = 20
mgMg.display()
#del mgMg.age

school = School()
school.enroll(mgMg)