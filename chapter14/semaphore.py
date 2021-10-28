from threading import *
import time

sem = Semaphore(2)

def one(thread_name):
    sem.acquire()
    print("Got lock ",thread_name)
    for i in range(1,100):
        print("Process ",thread_name," =>",i)
    print("release lock ",thread_name, " sem ",sem)
    sem.release()
    
t1 = Thread(target=one,args=("one",))
t2 = Thread(target=one,args=("two",))
t3 = Thread(target=one,args=("three",))

t1.start()
t2.start()
t3.start()