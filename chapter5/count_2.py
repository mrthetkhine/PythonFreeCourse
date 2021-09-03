str = "Welcome1 from Python programming Welcome"
print("Count Welcome ", str.count("Welcome"))
print("Count Welcome from 1 ", str.count("Welcome",1))

sub_string = "Welcome"
print("Welcome in str ", sub_string in str)

count = 0
index = 0
while index < len(str):
    another_str = str[index:index+len(sub_string)]
    print("Another sub ",another_str)
    if( sub_string in another_str):
        count = count+1
    index = index +1

print("Count ",count)