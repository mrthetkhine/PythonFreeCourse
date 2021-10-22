import pickle

#print("pickle ",pickle)
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age


#with open("human.data","wb")as file:
#    h  = Human("Python",40)
#    pickle.dump(h,file)
with open("human.data","rb") as file:
    h = pickle.load(file)
    print("h ",h.name ,' age ',h.age)