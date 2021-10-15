with open("write_file.py","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line,end='')
