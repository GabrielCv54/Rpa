import requests as r
import sqlite3
import io
import sys
from bs4 import BeautifulSoup
from docx import Document

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


countries = []
url = 'https://restcountries.com/v3.1/name/{name}'

def parte1_API_Rest():
    for i in range(0,3):
        name = str(input(f'Qual o nome do {i+1}° país?: '))
        countries.append(name)
        url = f'https://restcountries.com/v3.1/name/{name}'
        response = r.get(url)
        data = response.json()
        info = data[0]

        try:
            coin = list(info.get('currencies',{}).values())[0]
            language = list(info.get('languages',{}).values())[0]

        except:
            coin = {'Moeda não foi reconhecida'}
            language = {'A língua é desconhecida!!'}

        '''    print(f'País : {info['name']['common']}')
        print(f'Continente : {info['continents']}')
        print(f'Língua : {language}')
        print(f'Moeda : {coin}')'''

        return {
            'nome_oficial': info.get('name',{}).get('official'),
            'nome_comum': info.get('name',{}).get('common','n/a'),
            'capital':info.get('capital',['n/a'])[0],
            'continente':info.get('continents','n/a'),
            'região':info.get('region','n/a'),
            'população':info.get('population',0),
            'moeda':coin.get('symbol','?'),
            'idioma':language,
            'fuso horário':info.get('timezones','n/a')[0],
            'bandeira':info.get('flags',{}).get('png','')
        }

    conn = sqlite3.connect('Dados_países.db')
    cursor = conn.cursor()       
    cursor.execute('''
    CREATE TABLE pais(
    id INTEGER PRIMARY KEY AUTOINCREMENT,nome oficial TEXT,nome comum TEXT,capital TEXT,continente TEXT, região TEXT,população INT,area total FLOAT,moeda VARCHAR(20),idioma TEXT,fuso horário STRING,
    bandeira TEXT
    )
''')
    conn.commit()

    cursor.execute('''
          INSERT INTO país VALUES(?,?,?,?,?,?,?,?,?,?,?)
                   ''',info.get['name']['official'],info.get['name']['common'],info.get['capital'],info.get['continents'],info.get['region'],info.get['population'],info.get['area'],info.get[coin])


def parte2_web_scraping():
   book_url = 'https://books.toscrape.com/'
   for i in range(0,10):
    response = r.get(book_url)
    soup = BeautifulSoup(response.text,'html.parser')
    title = soup.find_all('h3')[i]
    price = soup.find_all('p',class_='price__color')[i]
    avaliable = soup.find_all('p',class_='star-rating Three')[i]
    disponibility = soup.find_all('p',class_='instock availability')[i]

   conn = sqlite3.connect('livros.db')
   cursor = conn.cursor()


parte1_API_Rest()
print(countries)


