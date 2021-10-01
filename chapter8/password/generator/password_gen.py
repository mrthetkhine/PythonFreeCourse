from random import *
import string

def gen_password(pwd_legth):
    pwd = ""
    for i in range(pwd_legth):
        if random() > 0.4:
            pwd += choice(string.ascii_letters)
        else:
            pwd += choice(string.digits)
    return pwd
    
print("Upper case ",string.ascii_uppercase)
print("Digit ",string.digits)
print("password 5=> ",gen_password(5))
print("password 10=> ",gen_password(10))