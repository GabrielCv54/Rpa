import requests as r

country = 'brazil'
url = f'https://restcountries.com/v3.1/name/{country}'
response = r.get(url)
data = response.json()

#exibição das informações
info = data[0]
print(f'Nome: {info['name']}')
print(f'Capital: {info['capital']}')
print(f'Região: {info['region']}')
print(f'Continente: {info['continents']}')