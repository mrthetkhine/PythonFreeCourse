read_file = open("Inheritance.class","rb")
write_file = open("Temp.class","wb")
data = read_file.read()
write_file.write(data)

read_file.close()
write_file.close()