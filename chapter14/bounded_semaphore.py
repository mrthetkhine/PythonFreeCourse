from threading import *
import time

sem = BoundedSemaphore(2)
print("Acquire 1")
sem.acquire()

print("Acquire 2")
sem.acquire()

print("Release 1")
sem.release()

#print("Release 2")
#sem.release()

print("Release 3")
sem.release()

print("Done")