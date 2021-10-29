import re,urllib
import urllib.request

web_url = "https://www.sgcarmart.com/main/index.php"
url = urllib.request.urlopen(web_url)
text = str(url.read())
#print("Text ",text)
title = re.findall("<title>.*</title>", text)
print("Title ",title)