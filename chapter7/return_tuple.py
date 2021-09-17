def min_max(a,b): #parameter
    if a < b: 
        return a,b
    else:
        return b,a
    print("Never run")

min, max = min_max(10,20) #arguments
print("Min ",min, " Max ",max)
