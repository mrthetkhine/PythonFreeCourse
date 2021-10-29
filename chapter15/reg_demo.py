import re

my_str = "foo123bar"
print("Search ",re.search('[0-9][0-9][0-9]', my_str))
print("Search ",re.search('[0-9][0-9][0-9]', "hello3456"))
print("Search ",re.search('[0-9][0-9][0-9]', "235Hello345"))

print("Search ",re.search('[abc]', "helloa"))

#135 335 553
print("Search ",re.search('[1357][1357][1357]', "hello553"))
print("Search ",re.search('[1357][1357][1357]', "hello5253"))

print("Search ",re.search('[a-z][1357][1357]', "hello51hello"))
print("Search ",re.search('1.3', "103"))
print("Search ",re.search('1.3', "1A3"))
print("Search ",re.search('1.3', "13A"))

print("Search ",re.search('^Java', "JavaScript"))
print("Search ",re.search('^Java', "Java"))
print("Search ",re.search('^Java', " Java"))

print("Search ",re.search('Java$', "Programing in Java"))
print("Search ",re.search('Java$', "Programing in JavaScript"))

print("Search ",re.search('[a-z]*[1-5]*', "program123ee"))
print("Search ",re.search('[a-z]*[1-5]*', "123ee"))
print("Search ",re.search('[a-z]*[1-5]*', ""))

print("Search ",re.search('[a-z]+[1-5]+', "program123ee"))
print("Search ",re.search('[a-z]+[1-5]+', "program"))

print("Search ",re.search('[a-z]+[1-5]?', "program1"))
print("Search ",re.search('[a-z]+[1-5]?', "program"))
print("Search ",re.search('[a-z]+[1-5]?', "program12"))

print("Search ",re.search('[0-9]{5}', "123456"))
print("Search ",re.search('[0-9]{2,6}', "123456"))
print("Search ",re.search('[0-9]{2,6}', "12e"))