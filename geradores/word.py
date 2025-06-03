from docx import Document

#1- criar um novo documento
document = Document()

#2 - Adicionar um título
document.add_heading("relatori",level=1)

#3- Adicionar parágrafo
document.add_paragraph("Este documento descreve o arquivo gerado durante a aula de rpa")

#4- Adicionar subtitulo
document.add_heading('Atividades',level=2)

#5 - Adicionando uma lista de atividades
activity = [
    "Reunião com a equipe ",
    "Desenvolvimento de novos módulos",
    "Testes de Funcionalidades",
    "Treinamento para novos colaboradores"
    ]

for act in activity:
    document.add_paragraph(act,style="List Bullet")

# 6 - Adicionar um subtítulo para considerações finais
document.add_heading('Considerações finais',level=2)

#7 - Parágrafo final com as considerações
document.add_paragraph('Todas as metas estabelecidas foram cumpridas')

#8- Salvar
document.save('relatór.docx')
print('Salvamento feito com sucesso!!')