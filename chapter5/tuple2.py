my_tuple = ()
print("Empty tuple ",my_tuple)

my_tuple = 2,
print("Single tuple ",my_tuple , " len ",len(my_tuple))

my_tuple = 2,"Hello"
print("Two element tuple ",my_tuple)

lst = [1,"Two",3]
my_tuple = tuple(lst)
print("Tuple constructor ",my_tuple)

one_to_ten = range(0,11)
my_tuple = tuple(one_to_ten)
print("Tuple constructor from range ",my_tuple)

print("Tuple [1] ",my_tuple[1])
print("Tuple [-1] ",my_tuple[-1])
print("Tuple [1:5] ",my_tuple[1:5])
print("Reverse Tuple [:-1] ",my_tuple[:-1])

