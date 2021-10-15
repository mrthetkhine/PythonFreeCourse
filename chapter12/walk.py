import os
for dir_path,dir_names,file_names in os.walk('./'):
    print("Dir path ",dir_path)
    print("Dir name ",dir_names)
    print("File name ",dir_names)