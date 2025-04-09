#Manipular arquivos csv
#Instalar a biblioteca pandas

import pandas as pd


#Dataframe de exemplo
books = [{'Autor':'Rick Riordan','Título':'Magnus chase','Ano':2016},
         {'Autor':'JK Rowling','Título':'Harry Potter e a Pedra filosofal','Ano':1997},
         {'Autor':'Christian Barbosa','Título':'A tríade do tempo','Ano':2008},
         {'Autor':'Edir Macedo','Título':'Como vencer as guerras pela fé','Ano':2019},
         {'Autor':'Sun Tzu','Título':'A arte da guerra','Ano':500},
          {'Autor':'Aldous Huxley','Título':'Admirável mundo novo','Ano':1932},
          {'Autor':'Miguel Cervantes','Título':'Dom Quixote','Ano':1605},
          {'Autor':"Antoine de Saint-Exupéry",'Título':'Pequeno Príncipe','Ano':1943}
         ]

#Criando o dataframe de livros
book_df = pd.DataFrame(books)
book_serie = pd.Series(books)
'''print('Dataframe criado!')
print(book_df)'''
#print(book_serie)

#Transformando esse dataframe em csv e excel
book_df.to_csv('livros.csv',index=False)
'''txt = pd.read_csv('arquivo.txt',sep='\t')
print(txt)'''
'''book_df.to_excel('livros2.xlsx',index=False)
print('Arquivo criado com sucesso nos formatos excel')'''
'''book_df_csv = pd.read_csv('livros.csv')
print(book_df_csv)'''


#ler e manipular do excel
new_df = pd.read_excel('livros.xlsx')#Lê a informação do excel
new_df['Ano'] = new_df['Ano'] + 1 #Simula a atualização do ano
new_df.to_excel("livros atualizados.xlsx")
#print(new_df)

#Lê as informações do arquivo em excel : livros2.xlsx
df_read = pd.read_excel('livros2.xlsx')
autores = book_df.loc[:,'Autor']
print(autores)
string = book_df.loc[6,'Autor']
print(string)

#print(new_df.head())
#print(new_df.shape) 
#print(new_df.describe())
#titles = book_df['Título']
#print(titles)

#print(new_df['Autor'])
#print(new_df.loc[new_df['Ano'] >= 2020, ['Título']])