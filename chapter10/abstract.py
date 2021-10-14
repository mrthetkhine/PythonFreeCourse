from abc import *
class Human(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def work(self):
        pass    
class Doctor(Human):
    def __init__(self):
        print("Doctor constructor")
    def work(self):
        print("Doctor work") 
class Teacher(Human):
    def __init__(self):
        pass
h = Doctor()
h.work()

#t = Teacher()