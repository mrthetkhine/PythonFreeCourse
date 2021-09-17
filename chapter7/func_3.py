def minimum(a,b):
    if a < b: 
        return a
    else:
        return b
    print("Never run")

result = minimum(10,20)
print("Min ",result)

print("Min 30,20 => ",minimum(30,20))