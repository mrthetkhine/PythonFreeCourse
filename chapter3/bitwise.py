x = 2
y = 3

print(" bin(2) ", bin(2))
print(" bin(3) ", bin(y))
print(" bin(2) & bin(3) ", 2 & 3)
print("True & False ", True & False)
#print("'True' & False ", 'True' & False)

def getTrue():
    print("Get True")
    return True
def getFalse():
    print("Get False")
    return False

print("getFalse() & getTrue() ", getFalse() & getTrue())
print("getTrue()| getTrue() ", getTrue()| getTrue())

print(" !bin(2) ", 2^3)
print(bin(2), ~2)

print(bin(2)," ", bin(2<<1), " ", 2<<2)
print(bin(8)," ", bin(8>>1), " ",8>>2)