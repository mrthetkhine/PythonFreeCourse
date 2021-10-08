class Engine:
    def __init__(self):
        print("Engine constructor")
    def start(self):
        print("Engine start")

class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        print("Car start")
        self.engine.start();
    
car = Car()
car.start()