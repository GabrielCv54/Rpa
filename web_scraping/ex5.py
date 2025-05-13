'''
Buscar noticias do site:
https://www.r7.com/
'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.r7.com/'#Sites reais podem exigir Headers
respose = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(respose.text,'html.parser')

for manchete in soup.find_all('article',class_='card-@container card-flex card-flex-col'):
    print(manchete.text.strip())