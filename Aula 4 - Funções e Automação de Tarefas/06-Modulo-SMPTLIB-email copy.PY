import smtplib
import getpass

def enviar_email():
    # Seu endereço de e-mail e senha
    meu_email = 'joao.araujo.bezerra@outlook.com'
    senha_email = getpass.getpass('Digite sua senha para continuar: ')

    # Lista de destinatários do e-mail
    lista_destinatarios = ['joao.araujo.bezerra@outlook.com', 'joaobosco.arabez@gmail.com']

    try:
        # Conexão com o servidor SMTP (no exemplo, usamos o Gmail)
        smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtp.starttls()
        smtp.login(meu_email, senha_email)

        # Criar mensagem
        assunto = 'Assunto do e-mail'
        conteudo = 'Conteúdo do e-mail'
        mensagem = f'Subject: {assunto}\n\n{conteudo}'

        # Enviar e-mail para cada destinatário
        for destinatario in lista_destinatarios:
            smtp.sendmail(meu_email, destinatario, mensagem)
            print(f'E-mail enviado para {destinatario}')

        # Fechar a conexão
        smtp.quit()
        print('E-mails enviados com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro ao enviar o e-mail: {str(e)}')

# Chamar a função para enviar o e-mail
enviar_email()