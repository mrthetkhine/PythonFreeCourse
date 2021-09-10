nested_list =[
              [1,2,3],
              [4,5,6],
              [7,8,9],
            ]
print("Nested list ",nested_list)
print("Row 0 ",nested_list[0])
print("Row [0][1] ",nested_list[0][1])
print("Row [2][2] ",nested_list[2][2])

for lst in nested_list:
    for item in lst:
        print("item ",item)
        
for row,row_item in enumerate(nested_list):
    print("Row ",row, "value ",row_item)
    for col,col_item in enumerate(row_item):
        print("Col ",col, " Item ",col_item)