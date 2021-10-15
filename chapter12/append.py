file = open("hello.txt","a")

messages = ["Apple","Orange"]
file.writelines(messages)

file.close()
