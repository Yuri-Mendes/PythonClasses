#enviando email

import smtplib #biblioteca para envio de emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

smtp_server= 'smtp-mail.outlook.com'
port=587

email='yt_evc@hotmail.com'
senha=getpass.getpass('Digite sua senha: ')
#print(f' usuario: {email}, senha: {senha_email}')

server=smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(email, senha)

mensagem=MIMEMultipart()
mensagem['From']='yt_evc@hotmail.com'
mensagem['To'] = 'yurinmendes61@gmail.com'
mensagem['Subject'] = 'Aula Email Python'
corpo= 'Este é o corpo do email.'
mensagem.attach(MIMEMultipart(corpo, 'plain'))

