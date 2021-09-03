my_list = [10,20,22,30,40]

user_no = int(input("Enter a number to find in list "))
found = False
index = 0

while not found and (index < len(my_list)):
    if my_list[index] == user_no:
        print("Found at index ",index)
        found = True
    else:
        index += 1

print("End of while")
