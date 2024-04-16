#Integração com txt e csv

"""Método Open -> Abre um arquivo em txt

arquivo=open('nomedo arquivo.txt,'r')
------------------------------------------

Médotodo With - Abre e fecha a conexão do arquivo

"""

# r - Abrir o arquivo para a leitura(read)
# w -Tem a função substituir conteudo do arquivo 
# a-  Adiciona uma informação no arquivo(append)

#a-  Adiciona uma informação no arquivo(append)
'''
with open('cliente.txt', 'a') as arquivo:
    arquivo.write('Aula de Python')
   ''' 
    
    
#Substitui o conteudo do arquivo
with open('cliente.txt', 'w') as arquivo:
    arquivo.write('Olá, seja bem vindo a aula de Python')




# #Lendo o arquivo

