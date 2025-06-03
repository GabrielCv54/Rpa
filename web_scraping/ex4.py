'''
coletar os titulos de livros
'''

import requests as r
from bs4 import BeautifulSoup
import sys
import io
import sqlite3 as sql
from openpyxl import workbook

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
 
url_books = 'https://books.toscrape.com'
response = r.get(url_books)
soup = BeautifulSoup(response.text,'html.parser')
books = soup.find_all('article',class_='product_pod')

for i in range(0,10):
        for book in books:
                title = book.h3.a['title']
                price = book.find('p',class_='price_color').text.plit()
                avaliable = book.find('i',class_='icon-star::before')
                disponibility = book.find('p',class_='instock availability').text.strip()
                print(f'Título: {title}')
                print(f'Preço : {price}')
                print(f'Avaliação : {avaliable}')
                print(f'Disponibilidade : {disponibility}')
                print('='*80)

conn = sql.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        título TEXT,
        preço FLOAT,
        avaliação TEXT,
        disponibilidade TEXT
        ) 
""")


cursor.execute('''
INSERT INTO livros(título,preço,avaliação,disponibilidade) VALUES(?,?,?,?)
''',(title,price,avaliable,disponibility))
conn.commit()

'''for book in books:
        title = book.find('a')['title']
        print(f'Título : {title}')'''