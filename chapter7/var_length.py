def our_sum(*numbers):
    print("Numbers ",numbers , 'type ',type(numbers))
    return sum(numbers)

print("Sum ",our_sum(1,2))
print("Sum ",our_sum(1,2,3,4))

number_tuple = 1,2,3,4,5
print("Sum ",our_sum(*number_tuple))