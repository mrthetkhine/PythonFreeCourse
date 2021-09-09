str = input ("Enter string ")
#print("Reverse ", str[::-1])
words = str.split()
result = ""
print("Words ",words)
for word in words:
    result = result +" "+ (word[::-1])
print("Result ",result)
#print([w[::-1] for w in words])