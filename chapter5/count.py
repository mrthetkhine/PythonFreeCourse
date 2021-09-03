str = "Welcome from Python programming Welcome"
print("Count Welcome ", str.count("Welcome"))
print("Count Welcome from 1 ", str.count("Welcome",1))

sub_string = "Welcome"
start_index = 0
count = 0
while str.find(sub_string,start_index) != -1:
    start_index = str.find(sub_string,start_index)+1
    count = count +1

print("Total count ",count)