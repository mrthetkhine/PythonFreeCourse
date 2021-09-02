myanmar = float(input("Enter mark for myanmar "))
english = float(input("Enter mark for english "))
math = float(input("Enter mark for math "))

if myanmar >= 40:
    if english >= 40:
        if math >= 40:
            print("Pass ")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")

print("Code end")