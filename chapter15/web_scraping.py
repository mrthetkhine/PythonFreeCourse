import requests
from bs4 import BeautifulSoup

# python3 -m pip install requests
# python3 -m pip install beautifulsoup4
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)