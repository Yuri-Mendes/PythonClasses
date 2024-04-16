
#enviando email

import smtplib #biblioteca para envio de emails
import getpass

email='yt_evc@hotmail.com'
senha_email=getpass.getpass('Digite sua senha: ')
#print(f' usuario: {email}, senha: {senha_email}')

#lista de destinatários

lista_destinatario=['yt_evc@hotmail.com']

smtp=smtplib.SMTP('smtp-mail.outlook.com', 587)
smtp.ehlo()#verifica a conexão do email
smtp.starttls()#verificar a ortografia do email
smtp.ehlo()#fecha a conexao
smtp.login(email, senha_email)

#criar a mensagem
assunto='Curso de Python'
conteudo='Email enviado com código Python'
mensagem=f'Subject: {assunto}\n\n{conteudo}'

for destinatario in lista_destinatario:
    smtp.sendmail(email,destinatario,mensagem)

#enviar email
smtp.quit()
