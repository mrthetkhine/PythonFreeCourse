from threading import *

class MyThread:
    def __init__(self,name):
        self.name = name
    def method(self):
        for i in range(1,50):
            print("Thread ",self.name, " i ",i)

objA = MyThread("ThreadA")
objB = MyThread("ThreadB")

threadA = Thread(target=objA.method)
threadB = Thread(target=objB.method)

threadA.start()
threadB.start()