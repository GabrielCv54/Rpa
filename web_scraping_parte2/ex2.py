#Navegar de forma automática até o fim do catálogo de 

import requests as r
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

page = 1
find = True

while find:
    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = r.get(url)
    
    if response.status_code != 200:
        break # A página for inexistente

    soup = BeautifulSoup(response.text,'html.parser')     
    books = soup.find_all('h3')   

    if not books:
        break #Não possui livros na página,encerra navegação

    print(f'\n Página {page}')
    for book in books:
        title = book.find('a')['title']
        print(f'Livro: {title}')
    page += 1