file = open("write_file.py","r")

ten_char = file.read(10)
print("Ten character ",ten_char)

line = file.readline()
print("Line ",line)

lines = file.readlines()
print("lines ",lines)

file.close()
