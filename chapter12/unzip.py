from zipfile import *

file = ZipFile("file.zip",'r',ZIP_STORED)
names = file.namelist()

for name in names:
    print("File name ",name)
    file_data = open(name,'r')
    print(file_data.read())
    file_data.close()
file.close()