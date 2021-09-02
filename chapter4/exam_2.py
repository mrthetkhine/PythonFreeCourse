myanmar = float(input("Enter mark for myanmar "))
english = float(input("Enter mark for english "))
math = float(input("Enter mark for math "))

if myanmar < 40 or english < 40 or math < 40:
    print("Fail")
else:
    print("Pass")

print("Code end")