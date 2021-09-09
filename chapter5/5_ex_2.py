str = input ("Enter string ")
#print("Reverse ", str[::-1])
print(" ".join([w[::-1] for w in str.split()]))