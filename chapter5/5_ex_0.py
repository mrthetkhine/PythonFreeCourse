str = input ("Enter string ")
#print("Reverse ", str[::-1])
words = str.split()
reversed_word = " ".join(words[::-1])
print("Words ",reversed_word)