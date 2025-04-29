'''
Coletar as citações do site
https://quotes.toscrape.com/
'''

import requests as r
from bs4 import BeautifulSoup

'''url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

for phrase in soup.find_all('span',class_='text'):
    print(phrase.text)'''

url = 'https://www.marvel.com/explore'
response = r.get(url)

soup = BeautifulSoup(response.text , 'html.parser')

characters = soup.find_all('a',class_='explore__link')

for character in characters:
    print(character.text.strip())