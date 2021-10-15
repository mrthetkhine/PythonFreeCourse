file = open("hello.txt","w")

file.write("Hello File write")
file.write("From Python")

for i in range(100):
    file.write(str(i)+"\r\n")

print("Writing done")
file.close()
