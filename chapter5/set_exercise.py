import operator

my_string = """
Programming in Java 
Programming in JavaScript with Node
Programming in Python with Danjo
"""
words = my_string.split()
print("Words ",words)

unique_words = set(words)
print("Unique word ",unique_words)

results =[ (w,my_string.count(w)) for w in unique_words]
results.sort(key=operator.itemgetter(1),reverse=True)
print("Result ",results)