import dis

a = 10
b = 20
dis.dis(compile("c=a+b*2",'','exec'))
print(dir())
