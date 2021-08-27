x = 10
y = 10

print("id x ",id(x), " id y ",id(y))
print("x is y ",x is y)

a = [10,20,30]
b = [10,20,30]
c = b
print("id(a) ",id(a), " id (b) ",id(b))
print("a is b ",a is b)
print("c is b ",c is b)

d = ()
e = ()
print("d is e ",d is e)

str1 = "Hello"
str2 = "Hello"
print("str1 is str2 ",str1 is str2)