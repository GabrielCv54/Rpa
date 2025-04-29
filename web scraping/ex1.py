from bs4 import BeautifulSoup
html='''
   <html>
    <body>
    <h1>Olá mundo</h1>
     <p class='mensagem'>Bem vindo ao web-scraping</p>
     <p class='teste'>Olá teste</p>
'''

soup = BeautifulSoup(html,'html.parser')
print(soup.h1.text)
print(soup.find('p').text)