'''
Coletar as citações do site
https://quotes.toscrape.com/
'''

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

for phrase in soup.find_all('span',class_='text'):
    print(phrase.text)