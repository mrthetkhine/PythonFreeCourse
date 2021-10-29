import re

print("Search ",re.search('[a-z]*\.py', "hello.py"))
print("Search ",re.search('[a-z]*\.py', "helloy"))

print("Search ",re.search('[a-z]{3,}\.(com|org|gov)', "hello.com"))
print("Search ",re.search('[a-z]{3,}\.(com|org|gov)', "hello."))
print("Search ",re.search('[a-z]{3,}\.(com|org|gov)', "hello.org"))

print("Search ",re.search('\w+', "hello_122"))
print("Search ",re.search('\W+', " #$$"))

print("Search ",re.search('\d{9,11}', "019292393333"))
print("Search ",re.search('\D+', "hello1233_"))

print("Search ",re.search('\s*hello', "how   hello"))
print("Search ",re.search('\S+', "hello1233_"))

print("Search ",re.search(r'\bworld', "helloworld "))