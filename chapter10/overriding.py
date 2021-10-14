class Human():
    def __init__(self):
        print("Human Constructor")
    def work(self):
        print("Human Work")
    def breath(self):
        print("Human breath")

class Doctor(Human):
    def __init__(self):
        print("Doctor Constructor")
    def work(self): #override
        super().work();
        print("Doctor Work")

d = Doctor()
d.work()
d.breath()