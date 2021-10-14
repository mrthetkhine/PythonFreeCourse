class InvalidOperand(Exception):
    def __init__(self,msg):
        self.msg = msg

def div(a,b):
    if b == 0:
        raise InvalidOperand("Divisor is zero")
    else:
        return a/b
try:
    print(div(10,0))
except InvalidOperand as err:
    print("Invalid operand ",err.msg)