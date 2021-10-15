import os
file_name = "hello1.txt"
if os.path.isfile(file_name):
    print("File exist")
else:
    print("File does not exist")