x = [0,10,25,200]
my_bytes = bytearray(x)
print("my_bytes ", my_bytes)
print("type my_bytes ", type(my_bytes))
print("type my_bytes ", my_bytes[1])

my_bytes[0] = 100
print("my_bytes ", my_bytes)
print("my_bytes ", my_bytes[0])