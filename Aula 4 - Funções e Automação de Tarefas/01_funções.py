"""
FUNÇÔES
Uma forma de organizar o código e garantir que ele 
possa ser reutilizado. Ideal que cada função seja 
responsável por uma tarefa...



>>>Sintaxe:
def nome_da_funcao(parametros):
    # Corpo da função
    # Instruções a serem executadas
    return valor_retornod
"""

# def: Palavra-chave usada para definir uma função.
 # nome_da_funcao: Nome dado à função para chamá-la posteriormente.
# parametros: Argumentos que a função pode receber (opcionais).
# return: Palavra-chave usada para retornar um valor da função (opcional).
    
    
    
    
# Função diz oi
# def dizerOi():
#     print('Oi, Usuário!')

# dizerOi()

# Função canta parabéns
# def parabens():
#     print('Parabéns pra você! Parabéns pra você!')

# parabens()

# Função soma 2 valores
# def soma():
#     a = 10
#     b = 20
#     resultado = a + b
#     return resultado
# print('Resultado da soma: {soma}')

# def soma():
#         a = int(input('Digite o 1º valor: '))
#         b = int(input('Digite o 2º valor: '))
#         resultado = a + b
#         print('Resultado da soma dos valores: {resultado}')
# soma()

# def soma():
#         a = int(input('Digite o 1º valor: '))
#         b = int(input('Digite o 2º valor: '))
#         resultado = a + b
#         print(resultado)
# soma()

'''1 -Exercicio : Média :Crie uma Função que Peça para o Usuario Entrar com 4 Notas, Se for >=7 aprovado Se não Reprovado '''

# def media():
#     nome = str(input('Digite o nome do aluno:')).title()
#     matricula = str(input('Digite a matricula do aluno:'))
#     nota1 = int(input('Digite a 1º nota: '))
#     nota2 = int(input('Digite a 2º nota: '))
#     nota3 = int(input('Digite a 3º nota: '))
#     nota4 = int(input('Digite a 4º nota: '))
#     calc_media = (nota1+nota2+nota3+nota4) / 4
#     if calc_media >= 7:
#         resultado ='Aprovado!'
#     else:
#         resultado = 'Reprovado'
#     print(f'\nEsta é a média final do aluno {nome} - {matricula}: {resultado} {calc_media:.2f}.\n')
# media()


'''2-Exercicio:IMMC: Crie a entrada do usuário com Peso e Altura , faça o calculo do IMMC e mostre o resultado '''
def imc():
    nome = str(input('Digite o nome:')).title()
    idade = str(input('Digite a idade:'))
    peso = int(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    calc_imc = peso / altura**2
    if calc_imc<18.5:
        resultado = 'Abaixo do peso.'
    elif 18.5 <=  calc_imc < 24.9:
        resultado = 'Peso Normal.'
    elif 24.9 <=  calc_imc < 29.9:
        resultado = 'Sobrepeso.'
    elif 29.9 <=  calc_imc < 34.9:
        resultado = 'Obesidade classe I.'
    elif 34.9 <=  calc_imc < 39.9:
        resultado = 'Obesidade classe II.'
    else:
        resultado = 'Obesidade classe III.'
    print(f'\nEste é o IMC do {nome}, idade: {idade} anos: {resultado} {calc_imc:.2f}.\n')
imc()
