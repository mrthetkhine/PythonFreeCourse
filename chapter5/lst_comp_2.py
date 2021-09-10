lst = ["apple","orange","banana","grapefruit"]
#[("APPLE",5),("ORANGE")]
lst_two = [(x.upper(),len(x))for x in lst if len(x)>5]
print("lst two ",lst_two)

marks = [("mayan",30),
         ("eng",40),
         ("math",90),
         ]
pass_subject = [subject for subject in marks if subject[1]>=40]
print("Pass subject ",pass_subject)

pass_exam = len(marks) == len(pass_subject)
print("Pass ",pass_exam)