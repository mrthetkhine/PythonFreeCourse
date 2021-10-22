from threading import *

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        for i in range(1,50):
            print("Thread ",self.name, " i ",i)

threadA = MyThread("ThreadA")
threadB = MyThread("ThreadB")

threadA.start()
threadB.start()
print("Active count ",active_count())