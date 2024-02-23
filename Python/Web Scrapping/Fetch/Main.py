from bs4 import BeautifulSoup as b
import requests as r

source = "https://www.geeksforgeeks.org/python-programming-language"

data = r.get(source)

soup = b(data.content, 'html.parser')
tags = soup.find_all('h1')

for tag in tags :
    print(tag.text)