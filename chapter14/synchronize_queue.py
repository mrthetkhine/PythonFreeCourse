from threading import *
import queue
import random

#items = queue.Queue()
#items = queue.LifoQueue()
items = queue.PriorityQueue()

class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            items.put(item)
            print("Item Produce ",item)
                
class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        for i in range(10):
            item = items.get()
            print("Item consume ",item)
                
producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()