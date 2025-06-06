import sys
import io
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

try:
    print('Aguarde, o email está sendo enviado!!')
    server_email = smtplib.SMTP('smtp.gmail.com',port=587)
    server_email.starttls()
    server_email.login(user='gabriel.carvalhovieira123@gmail.com'
,password='uujl zmed qyfk onkt')

    #Montar email
    sender = 'gabriel.carvalhovieira123@gmail.com'
    recipient = ['gabriel.carvalhovieira123@gmail.com','gabriel.cvieira@aluno.faculdadeimpacta.com.br']
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ", ".join(recipient)
    message['Subject'] = 'Smtplib email'

    body = 'Estou enviando um segundo email para realizqr o envio desse email'
    message.attach(MIMEText(body,'plain'))

    #Enviar o email
    server_email.sendmail(sender,recipient,message.as_string())

    print('E-mail enviado !!')
except Exception as erro:
    print(f'Erro: {erro}')