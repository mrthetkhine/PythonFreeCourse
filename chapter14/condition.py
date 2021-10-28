from threading import *
import time
import random

items = []
condition = Condition()

class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        for i in range(10):
            time.sleep(1)
            with condition:
                item = random.randint(0, 256)
                items.append(item)
                print("Produce ",item)
                condition.notify()
                
class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        for i in range(10):
            with condition:
                print("Consumer waiting")
                condition.wait()
                item = items.pop()
                print("Item consume ",item)
                
            

producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()