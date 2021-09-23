my_lst = [1,2,3,4,5,6,7,18,19,21,33]
print(" my_list ",my_lst)
incOne = lambda x: x+1
def is_even(x):
    print("Chcek is_even ",x , " ", x%2 ==0)
    return x%2 == 0

print("increase one to all element ", list(map(incOne,filter(is_even,my_lst))))