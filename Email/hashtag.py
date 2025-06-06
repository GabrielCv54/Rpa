import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

body = '''
<h1>Título do email</h1>
<p>Como vão meus amigos?</p>
'''

msg=  MIMEMultipart()