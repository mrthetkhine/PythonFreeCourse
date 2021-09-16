def division(num,divisor):
    if divisor == 0:
        return "Division by zero error",0
    else:
        return None,num/divisor

print("Division ",division(3,2))
err , result =  division(3,0)
if(not err):
    print("Result is ",result)
else:
    print("Error ",err)