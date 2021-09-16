my_tuple = ()
print("Empty tuple ",my_tuple)
one_to_ten = range(0,11)
my_tuple = tuple(one_to_ten)
print("Tuple constructor from range ",my_tuple)

#my_tuple[1] = "Change"
another_tuple = ([1,2,3,4,5,6],"Another")
print("Another tuple ",another_tuple)
#another_tuple[0] = []
another_tuple[0].append(100) 
print("Another tuple ",another_tuple)