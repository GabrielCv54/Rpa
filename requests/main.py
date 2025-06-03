import requests as r
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


url = 'https://httpbin.org/get'
dados = {
         'Id':1,
         'Nome':'Eduardo',
         'Idade':19,
         'Faculdade':'Faculdade USP',
         'Curso':'Ciencia da computação',
         'Cidade':'RJ',
         'RA':115550
         }

dados_2 = {
     'Id':2,
     'Nome':'Ana',
     'Idade':20,
     'Faculdade':'Faculdade Impacta',
     'Curso':'Sistemas da Informação',
     'Cidade':'São Paulo -SP',
     'RA':2569872
}

new_data = {
  'Id':3,
  'Nome':'Jonatas',
  'Idade':21,
  'Faculdade':'Faculdade Belas artes',
  'Curso':'Direito',
  'Cidade':'Osasco-SP',
  'RA':2669854
}
headers = {'Content-Type':'application/json'}

#GET
try:
   response = r.get(url,params=dados)
   if response.status_code == 200:
       print('Dados :')
       print(response.json())
   else:
       print(f'Erro na requisição GET : {response.status_code}')
except r.exceptions.RequestsWarning as e:
    print(f'Erro inesperado : {e}')

#POST
"""try:
  response = r.post(url,json=(dados,dados_2),headers=headers)

  if response.status_code == 200:
    print('Novos dados adicionados com sucesso!!✅')
    print(response.json())
  else:
    print(f'Erro de requisição POST: {response.status_code}')
    print(response.text)

except r.exceptions.HTTPError as erro:
  print(f'Erro: {erro}')

try:
   response = r.post(url,json=new_data,headers=headers)
   if response.status_code == 200:   
      print('Dados adicionados')
      print(response.json())
   else:
     print(f'Erro na requisição POST : {response.status_code}')
except r.exceptions.RequestsWarning as er:
   print(f'Erro na requisição : {response}')"""


data_update = {
         'Id':1,
         'Nome':'Gabriel Carvalho Vieira',
         'Idade':19,
         'Faculdade':'Faculdade Fiap',
         'Curso':'Análise e Desenvolvimento de Sistemas',
         'Cidade':'São Paulo - SP',
         'RA':2401423
         }

#PUT
"""try:
    response = r.put(url,json=data_update,headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        print('Recurso atualizado✅')
        data = response.json()
        print(data)
    else:
        print(f'Erro na requisição PUT : {response.status_code}')
        print(response.text)
except r.exceptions.RequestException as error:
    print(f'Erro na requisição : {error}')
"""

#DELETE
'''try:
    response = r.delete(url,params=dados)
    
    if response.status_code == 204 or response.status_code == 200:
        print('Dados deletados!!!✅ ')
        print(response.json())
    else:
        print(f'Erro na requisição DELETE : {response.status_code}')
        print(response.text)

except r.exceptions.RequestException as erro:
    print(f'Erro : {erro}')'''