str = "Apple Orange Banana"
str_list = str.split()
print("str_list ",str_list)
print("str ",str)

date_str = "3-08-2021" #3/08/2021
date_str_list = date_str.split("-")
print("date list ",date_str_list)

date_str_new = '/'.join(date_str_list)
print("date str new ",date_str_new)