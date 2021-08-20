import sys

x  =10
print("get size of number ",sys.getsizeof(x))

x = 10.2
print("get size of float ",sys.getsizeof(x))

c = 100293939393
print("get referene count ",sys.getrefcount(c))