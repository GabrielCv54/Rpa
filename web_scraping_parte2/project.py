'''
Este exemplo gera um pequeno menu onde o usuário escolhe como vai ser a navegação , e se quer exportar as informações para o excel ou para PDF
'''
import requests as r
from bs4 import BeautifulSoup
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#Funcão que extrai os livros
def book_exctract(page):
    try:
        url = f'https://books.toscrape.com/catalogue/page-{page}.html'
        response = r.get(url)
        if response.status_code != 200:
            return []
        
        soup =BeautifulSoup(response.text,'html.parser')
        books = []
        for article in soup.find_all('article',class_='product_pod'):
            title = article.h3.a['title']
            price = article.find('p',class_='price_color').text.strip()
            disponible = article.find('p',class_='instock availiability')
            books.append({
                'Título':title,
                'Preço':price,
                'Disponibilidade':disponible
            })
        return books
    except Exception as e:
        print(f'Erro ao extrair livros da página {page} : {e}')
        return []

#Função para exportar pra excel
def exportExcel(data , archive_name = 'livros.xlsx'):
    try:
        df = pd.DataFrame(data)
        df.to_excel(archive_name,index=False)
        print('Arquivo Salvo!!')
    except Exception as erro:
        print(f'Erro na exportação : {erro}')

def menu():
    print('''
==============================
    PROJETO SCRAPING DE LIVROS
==============================
    [1] Buscar livros de 1 página
    [2] Buscar livros de múltiplas páginas
    [3] Exportr dados para o excel
    [4] Exportar dados para o PDF
    [0] Sair  
''')
    
menu()