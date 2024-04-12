"""

Print:
    Função responsável por imprimir informações no console, mensagem para o usuário.
"""

print('Olá Mundo')

#Armazenar um Numero(Int)
valor = 20
print(valor)

#Armazena um Texto (String)
nome='joão da silva'
rua='joão melo da camara'
print('Seu nome é ' + nome + '.' + ' Sua rua é ' + rua)
#pode se usar a vírgula no lugar do + para concatenar

#Armazenar um Float(.) Ponto flutuante para valores, decimais
salario=1.000
reajuste=0.05
#não usuar virgulas, mas sim ponto.

# Fstring (Mais usual)
nome='aline da silva'
endereco='rua 2'
bairro='pirituba'
print(f'Seu nome é {nome}, seu endereço é {endereco}, seu bairro é {bairro}')

#exiba para o usuario nome, sobrenome, idade e endereço
#\n para quebrar a linha
nome='higor'
sobrenome='silva'
idade=42
logradouro='Rua abacaxi'
numero=178
bairro='agrindus'
cidade='SP'
print(f'Seu nome é {nome} {sobrenome}\nSua idade é {idade} anos\nSeu endereço é {logradouro} {numero} {bairro} {cidade}')


"Funções de Formatações "
#upper , Lower ,Title , capitalize

nome="CUrso dE PyThoN"
print(nome.upper()) #texto em maiúsculo
print(nome.lower()) #texto em minúsculo
print(nome.title()) #Primeira letra em maiúsculo
print(nome.capitalize()) #Só a primeira letra em maiúsculo