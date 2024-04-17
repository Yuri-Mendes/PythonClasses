import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo):
    smtp_server = 'smtp-mail.outlook.com'
    port = 587
    username = 'yt_evc@hotmail.com'
    password = 'senha'
    server = smtplib.SMTP(smtp_server, port)
    server.starttls
    server.login(username, password)
    mensagem = MIMEMultipart()
    mensagem['From'] = 'yt_evc@hotmail.com'
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo, 'plain'))
    server.sendmail('yt_evc@hotmail.com','yurinmendes61@gmail.com',mensagem.as_string())
    server.quit()

destinatarios=[
    ['Maria','maria@exemplo.com'],
    ['Joana','joana@exemplo.com'],
    ['Henrique','henrique@exemplo.com'],
    ['Caio','caio@exemplo.com']
]

assunto = 'Assunto do email corporativo'
corpos = [
    'Olá, esse é o e-mail 1.',
    'Olá, esse é o e-mail 2.'
]

for i, destinatario in enumerate(destinatarios):
    corpo = corpos[i]
    enviar_email(destinatario, assunto, corpo)
    print(f'E-mail enviado para: {destinatario}')
