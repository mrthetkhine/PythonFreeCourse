from threading import *

def method1():
    for i in range(1,40):
        print("Child Thread ", i)
thread = Thread(target=method1)
thread.start()
for i in range(1,40):
    print("Main Thread ", i)
    