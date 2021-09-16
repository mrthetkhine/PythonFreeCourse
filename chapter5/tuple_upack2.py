my_tuple = "Aung Aung",23,"Description"
name,age,_ = my_tuple #name = my_tuple[0], age = my_tuple[1]

print("Name ",name, " Age ",age)
name = name.upper
print("My Tuple ",my_tuple)

my_lst = [1,2,2,3]
another_tuple = (my_lst,1)
another_lst,_= another_tuple

another_lst[0] = 100
print("Another list ",another_lst)
print("My list ",my_lst)
print("Another list is my_lst",another_lst is my_lst)

def process(*argv):
    print("Argv ",argv, type(argv))
process(1,2,"Hello")