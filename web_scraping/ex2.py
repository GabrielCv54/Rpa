import requests as r
import json
from bs4 import BeautifulSoup

url = 'https://httpbin.org/put'
'''response = r.get(url)
soup = BeautifulSoup(response.text,"html.parser")

promisse = soup.find('p',class_="m-promises-text is-fz-20 is-fw-500")
print(promisse)'''


#Requisição de uma API
'''url='https://api.agify.io/?name=Gabriel'
response = r.get(url)
json = response.json()
print(json)'''

#Enviar dados para a API - Post
'''url='https://httpbin.org/post'
data = {'nome':'Junior','idade':22,'Curso':"ADS","Cidade":'Rio de Janeiro',"Faculdade":"UFRJ"}
response = r.post(url,data,headers={"User-Agent":"GCV"},cookies={"Nome":"Tropa dos devs"})
print(response.json())'''

'''params = {"Language":"python","example":15}
response = r.get('https://httpbin.org/post',params=params)
print(response.text)'''

'''url2 = 'https://httpbin.org/basic_auth/GCV/'
request = r.post(url2,auth=("GCV"))
print(request.text)'''

#Verificação do site
'''url = 'https://www.impacta.edu.br/'
response = r.get(url)

if response.status_code == 200:
    print('Site está online!!')
else:
    print('Site está offline!')'''

'''
url = 'https://httpbin.org/post'
data = {'Filme':'John Wick 3 Parabellum'}
response = r.post(url,data)

print(response.raise_for_status())'''

try:
    resposta = r.get(url)
    r1=resposta.json()
    print(r1)
except Exception as e:
    print(f'Erro:{e}')

try:
    new_data = {'Nome':'Guilerme Alves', 'Idade':47}
    response = r.post(url,new_data)
    print(response.text)
    print(response.raise_for_status())
except r.exceptions.RequestException as error:
    print(f'Erros na requisição : {error}')


updated = {'Nome':'João Pedro kauan','Idade':41}
headers = {'Content-Type':'application/json'}

try:
    response2=r.put(url,data=json.dumps(updated),headers=headers)
    response2.raise_for_status()

    print(f'Json: {response2.json()}')
    print(f'Headers {response2.headers}')

except Exception as e:
    print(f'Requisição com algum erro : {e}')