import math
from random import *

def toRadin(deg):
    return (deg* math.pi)/180

print("Sqrt ",math.sqrt(9))
print("Cos 90 deg ",math.cos( toRadin(90)))

print("Log ",math.log(9))

for i in range(0,11):
    r = random()
    #print("Random ",r)
    #print("Random int ",randint(1,11))
    #print("Uniform random ",uniform(1,11))
    print("Random range ",randrange(1,15,2))
    
lst = ["apple","orange","banana","fruit"]
