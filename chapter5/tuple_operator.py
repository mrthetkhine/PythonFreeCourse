one_to_ten = range(0,5)
my_tuple = tuple(one_to_ten)
print("Tuple constructor from range ",my_tuple)

another_tuple = tuple(range(20,25))
print("Another tuple ",another_tuple)

third_tuple = my_tuple + another_tuple
print("Third tuple ",third_tuple)

fruits = ("Orange","Apple","Banaa")
fruits_repeated = fruits * 3
print("Fruit repeated ",fruits_repeated)
print("Fruit repeated len ",len(fruits_repeated))
print("Fruit repeated count(Apple) ",fruits_repeated.count("Apple"))

print("Fruit repeated index(Apple) ",fruits_repeated.index("Apple"))

#print("Fruit repeated index(Apple) ",fruits_repeated.index("Apple1"))
print("String index ","Hello".find("Hello1"))

another_tuple = (1,2,3,4,5)
sorted_tuple = sorted(another_tuple)
print("Sorted ",sorted_tuple)
print("Min ",min(another_tuple))
print("Max ",max(another_tuple))

string_tuple = "One","Two","Three"
print("Sorted string ",sorted(string_tuple))