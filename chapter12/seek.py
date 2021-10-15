with open("hello.txt","w") as file:
    file.seek(10,0)
    file.write("hello")
