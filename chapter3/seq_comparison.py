lst1 = [10,20,60]
lst2 = [10,20,60]

#step 1pairwise comparison
#go next element if the element are same
#   if the list is shorter then smaller
print("[10,20] > [10,20,30] ", [10,20] > [10,20,30]) #len(first) > len(second)
print("[10,20] > [5,20,30] ", [10,20] > [5,20,30]) #10 > 5
print("[10,5] < [10,20,30] ", [10,5] < [10,20,30]) # 5 < 20

print("[10,20] >= [10,20,30] ", [10,20] >= [10,20,30])
print("[10,20] >= [5,20,30] ", [10,20] >= [5,20,30])

tp1 = (10,20,60)

print("lst1 > tp1 ",lst1 == tp1)