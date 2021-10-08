class Parent:
    var_one = "var one of Parent"
    def __init__(self):
        print("Parent")
        self.var_two = "instance of Parent"
        
    def instance_method(self):
        print("Parent instance method")
    @classmethod
    def class_method(cls):
        print("Parent class method")
    @staticmethod
    def static_method():
        print("Parent static method")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
    def method(self):
        print("Super varone ",super().var_one)
        #print("Super varone ",super().var_two)
        super().class_method()
        super().static_method()
        
    @classmethod
    def child_class_method(cls):
        pass
        #super().instance_method()

    @staticmethod
    def child_static_method():
        #super(Child,Child).instance_method()
        super(Child,Child).class_method()
c = Child()
c.method()
#c.child_class_method()
c.child_static_method()