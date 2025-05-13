from bs4 import BeautifulSoup
html='''
   <html>
    <body>
    <h1>DOCS</h1>
    <h2>Dattebayo API Documentation</h2>
     <p class='mensagem'>Welcome to the Dattebayo API documentation! This documentation provides a comprehensive guide to accessing data from the Naruto universe via our API. The base URL for the API is https://dattebayo-api.onrender.com.</p>
     <ol>
     <li><a href="docs#introduction">Introduction</a></li>
     <li><a href="docs#collections">Collections</li>
        <ul><a href="docs#characters">Characters</ul>
     </ol>
     <p class='message'>Melhores momentos em que eu aprendo a ser melhor</p>
     </body>
   </html>
'''

#Meus primeiros passos com BeautifulSoap
'''soup = BeautifulSoup(html,'html.parser')
print(soup.p['class'])
#print(soup.find('p').text)

for link in soup.find_all('a'):
    print(f"O link da tag a {link.get_text()} é {link.get('href')}")
    print(link.get_text())
    print('*'*len(link.get_text()))'''

'''with open("index.html",'r') as h:
    soup = BeautifulSoup(h,'html.parser')
   
print(soup)'''


css = BeautifulSoup(html,'html.parser')
print(css.p['class'])