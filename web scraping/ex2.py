import requests as r

'''url = 'https://www.universal.org/caixa-de-promessas/'
response = r.get(url)
print(response.text)
'''

#Requisição de uma API
'''url='https://api.agify.io/?name=Gabriel'
response = r.get(url)
json = response.json()
print(json)'''

#Enviar dados para a API - Post
'''url='https://httpbin.org/post'
data = {'nome':'Junior','idade':22}
response = r.post(url,data)
print(response.json())'''


#Verificação do site
url = 'https://www.impacta.edu.br/'
response = r.get(url)

if response.status_code == 200:
    print('Site está online!!')
else:
    print('Site está offline!')