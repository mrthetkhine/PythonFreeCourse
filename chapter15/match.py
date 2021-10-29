import re

m = re.match('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com something")
print("Match start ",m.start() , "end ",m.end())

m = re.fullmatch('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com something")
print("Match start ",m)

lst = m = re.findall('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com something http://www.yahoo.com")
for item in lst:
    print("Match ",item)
    
iter = m = re.finditer('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com something http://www.yahoo.com")
for item in iter:
    print("Match ",item)
    
replaced = re.sub('(http|https)://(www\.\w+\.(com|org|gov))','domain', "http://www.google.com something http://www.yahoo.com")
print("replaced ",replaced)

replaced = re.subn('(http|https)://(www\.\w+\.(com|org|gov))','domain', "http://www.google.com something http://www.yahoo.com")
print("replaced ",replaced)

lst_str = re.split("\.", "www.google.com")
for s in lst_str:
    print("Str ",s)