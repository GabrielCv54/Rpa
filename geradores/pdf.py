from reportlab.pdfgen import canvas

'''#1 - Criar o arquivo pdf
pdf = canvas.Canvas("exemplo.pdf")

#2 - Definir um título
pdf.setTitle('Relatório de Atividades')

#3- Inserir texto
pdf.drawString(100, 750, "Relatórios - Abril/2025")

#4- Inserir subtítulo
pdf.setFont("Helvetica",16)
pdf.drawString(100,720,"Atividades realizadas")

#5 - lista de atividades
activity = [
    "- Programando o back-end",
    "- Desenvolvendo o layout da página web",
    "- Reunião com a equipe",
    "- Apresentação a diretoria",
    "- Finalização"
]

#Escrever as atividades no PDF
y = 700 #definir a posição
for act in activity:
    pdf.setFont("Helvetica",14)
    pdf.drawString(120, y, act)
    y-=20

#6 - Salva
pdf.save()
print("Arquivo salvo com sucesso !!")'''


c = canvas.Canvas('texto.pdf')
c.drawString(100,250,'Este é um pdf que está sendo gerado com a biblioteca reportlab')