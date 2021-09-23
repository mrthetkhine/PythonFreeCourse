my_lst = [1,2,3,4,5,6,7,18,19,21,33]
print(" my_list ",my_lst)

def get_even(lst):
    even_list = []
    for ele in lst:
        if(ele %2 == 0):
            even_list.append(ele)
    return even_list

print("Even list ", get_even(my_lst))
#is_even = lambda x : x %2 == 0
def is_even(x):
    print("Chcek is_even ",x , " ", x%2 ==0)
    return x%2 == 0
print("Is even 10=>",is_even(10))
print("Is even 5=>",is_even(5))

is_odd = lambda x : not is_even(x)
is_gt_5 =  lambda x : x > 5
print("Is odd 5=>",is_odd(5))
print("Even using filter ", list(filter(is_even,my_lst)))
print("Odd using filter ", list(filter(is_odd,my_lst)))
print("Even list greter than 5 ", list(filter(is_gt_5, list(filter(is_odd,my_lst)))))