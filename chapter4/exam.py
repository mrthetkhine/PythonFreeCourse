myanmar = float(input("Enter mark for myanmar "))
english = float(input("Enter mark for english "))
math = float(input("Enter mark for math "))

pass_mark = 40
if myanmar >= pass_mark and english >= pass_mark and math >= pass_mark:
    print("Pass the exam")
else:
    print("Fail")

print("Code end")