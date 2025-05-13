import requests as r
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')

code = "USA"
url= f'https://restcountries.com/v3.1/alpha/{code}'
response = r.get(url)
data = response.json()

info = data[0]

print(f'Nome : {info['name']['common']}')
print(f'Moeda: {list(info['currencies'].keys())[0]}')