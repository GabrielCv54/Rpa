import requests as r

response = r.get('https://dattebayo-api.onrender.com/characters/547')
print(response.status_code)


'''url = 'https://httpbin.org/post'
dados = {'Nome':'Gabriel Carvalho Vieira','Idade':18,'Faculdade':'Faculdade Impacta de Tecnologia','Curso':'Análise e Desenvolvimento de Sistemas'}
response = r.post(url,dados)
print(response.json())'''
