def fact(n):
    if n == 1: #base case
        return 1
    else:
        return n * fact(n-1)

#print("3 ! =>", fact(998))
def imp_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print("Fact 998 ", imp_fact(1998))