from threading import *
import time
import random

items = []

class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            items.append(item)
            print("Produce ",item)
            time.sleep(1)


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        for i in range(10):
            item = items.pop()
            print("Item consume ",item)
            #time.sleep(1)

producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()