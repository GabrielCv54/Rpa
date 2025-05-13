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

url = 'https://www.cursoemvideo.com/cursos/'
response = r.get(url)

soup = BeautifulSoup(response.text , 'html.parser')

characters = soup.find_all('div',class_='fl-row-content-wrap')

for character in characters:
    print(character.text.strip())