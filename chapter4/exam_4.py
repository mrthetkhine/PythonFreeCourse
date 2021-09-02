number_of_subject = int(input("Enter number of subject "))
#marks = []

pass_mark = 40
isPass = True

for i in range(number_of_subject):
    mark = float(input("Enter mark for subject "+str(i)+" ") )
    isPass = isPass and mark >=40

if isPass:
    print("Pass the exam ")
else:
    print("Fail the exam")