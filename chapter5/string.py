str = "Hello"
print("index 0=> ",str[0])
print("index 1=> ",str[1])
print("index -2=> ",str[-2])
#print("index 5=> ",str[5])

for i in range(1,len(str)+1):
    print(str[-i])