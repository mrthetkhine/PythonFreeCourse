class Engine:
    def __init__(self):
        print("Engine constructor")
    def start(self):
        print("Engine start")

class DieselEngine:
    def __init__(self):
        print("DieselEngine constructor")
    def start(self):
        print("DieselEnginestart")

class Car:
    def __init__(self,engine):
        self.engine = engine
    def start(self):
        print("Car start")
        self.engine.start();
    
dieselEngine = DieselEngine() #inversion of control
engine = Engine()
car = Car(engine)
car.start()