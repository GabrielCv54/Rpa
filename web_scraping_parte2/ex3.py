#Exemplo navegar e extrair links de detalhes
import requests as r
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
base_details = 'https://books.toscrape.com/catalogue/'

for page in range(1,10):
    url = base_url.format(page)
    response = r.get(url)
    soup = BeautifulSoup(response.text ,'html.parser')

    print(f'\n Página {page}')
    books = soup.find_all('h3')
    for book in books:
        link = book.find('a')['href']
        title = book.find('a')['title']

        #Ajusta o detalhe do link para detalhes
        url_detail = base_details + link
        print(f'{title} --> {url_detail}')