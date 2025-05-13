'''
1-Coleta dos dados;
2- Criação e a conexão com o banco de dados;
3- Inserção dos dados;
4-Consultar o banco;
'''

import requests as r
import sqlite3

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#1
country ='Japan'
url = f'https://restcountries.com/v3.1/name/{country}'
response = r.get(url)
data = response.json()

info = data[0]
name = info['name']['common']
capital = info['capital'][0] if 'capital' in info else 'N/A'
region = info['region']
population = info['population']
coin = info['currencies']

print('dados extraidos')
print(f'Nome:{name}')
print(f'Região : {region}')
print(f'População : {population}')

#2- BD(SQLite);
connection = sqlite3.connect('paises.db')
cursor = connection.cursor()

#2.1 - Criação da Tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS paises(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               capital TEXT,
               regiao TEXT,
               população INTEGER
               )
               ''')

#3-Inserção
cursor.execute('''
        INSERT INTO paises(nome,capital,regiao,população) 
               VALUES(?,?,?,?)
''', (name,capital,region,population))
connection.commit()

#4- Consulta
print('Dados inseridos no Banco:')
cursor.execute('SELECT * FROM paises WHERE nome = ?',(name,))
for line in cursor.fetchall():
    print(line)

#Fechar conexão com o BD
connection.close()