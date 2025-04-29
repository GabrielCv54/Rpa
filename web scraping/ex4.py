'''
coletar os titutlos de livros
'''

import requests
from bs4 import BeautifulSoup

url_books = 'https://books.toscrape.com'
response = requests.get(url_books)
soup = BeautifulSoup(response.text,'html.parser')

titles = soup.find_all('h3')
for title in titles:
    print(title.a['title'])