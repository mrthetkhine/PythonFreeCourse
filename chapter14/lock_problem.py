from threading import *
import time

lock = Lock()

def factorial(n):
    print("Try to get lock for n ",n)
    lock.acquire()
    print("Get lock for n ",n)
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        lock.release()
        return result

print("Factorial ",factorial(3))