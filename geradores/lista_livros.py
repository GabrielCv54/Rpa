import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font


def exctract_data(url_base, url_page):
    response = requests.get(url_base + url_page)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article',class_='product_prod')
    
    data = []

    for book in books:
        title = book.h3.a['title']
        price = book.find('p',class_='price_color').text
        disponibility =book.find('p',class_="instock availiability").text.strip()
        link = url_base + book.h3.a['href']

        data.append({
            "Título":title,
            "Preço":price,
            "Disponbilidade":disponibility,
            "Link": link
        })
    return data

# 1 - Url Base
url_base = "https://books.toscrape.com/"

#2- começar a extração
all_books = []

for page in range(0,4):
    if page == 1:
        url_page = "index.html"
    else:
        url_page = f"catalogue/page-{page}"
    books_page = exctract_data(url_base,url_page)
    all_books.extend(books_page)

#3 - Criar o dataframe
df = pd.DataFrame(all_books)

#4- Salvar o Excel
df.to_excel('relatório_livros.xlsx',index=False, engine='openpyxl')

print('Relatório Salvo!!')