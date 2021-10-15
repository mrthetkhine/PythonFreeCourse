file = open("write_file.py","r")

lines = file.readlines()
for line in lines:
    print(line,end='')

file.close()
