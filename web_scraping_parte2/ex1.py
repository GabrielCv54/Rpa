#Navegar entre várias páginas e coletar algumas informações

import requests
import sys
from bs4 import BeautifulSoup
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

#Percorre as 3 primeiras páginas
for page in range(1,4):
    url = base_url.format(page)
    print(f'\n Página {page} - {url}')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('h3')

    for book in books:
        title = book.find('a')['title']
        print(f'Título : {title}')