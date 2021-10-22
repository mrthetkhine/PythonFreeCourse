import threading
#threading.currentThread().setDaemon(True)
threading.currentThread().setName("My Main Thread")
print("Current Thread ",threading.currentThread().getName())
print("Thread Id ",threading.currentThread().ident)
print("is daemon ",threading.currentThread().isDaemon())