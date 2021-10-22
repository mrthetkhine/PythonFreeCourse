from threading import *
import time

def double(n):
    for i in range(0,n):
        print("I am double => ",i*2)
        time.sleep(1)

def square(n):
    for i in range(0,n):
        print("I am square => ",i*i)
        #time.sleep(1)

start_time = time.time()
threadA = Thread(target=double,args=(5,))
threadB = Thread(target=square,args=(5,))

threadA.start()
threadB.start()

print("Active count ",active_count())
print("ThreadA is alive  ",threadA.is_alive())
print("ThreadB is alive ",threadB.is_alive())

thread_list = enumerate()
for thread in thread_list:
    print("Thread ", thread.name,  ' is daemon ',thread.isDaemon())
   

threadA.join()
threadB.join()

print("Active count ",active_count())
for thread in thread_list:
    print("After Thread ", thread.name)
end_time = time.time()
print("Time ",end_time - start_time)