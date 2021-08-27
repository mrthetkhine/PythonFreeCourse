x = 1
y = 2

temp = x
x = y
y = temp

print("x ",x)
print("y ",y)

x,y = y,x
print("x ",x)
print("y ",y)