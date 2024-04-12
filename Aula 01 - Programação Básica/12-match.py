"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
# Calculadora

# menu=int(input(f'[1]soma | [2]multiplicação | opção'))
# num1 = float(input('Informe um número:'))
# num2 = float(input('Informe um número:'))

# match menu:
#     case 1:
#         print(f'Resultado da soma dos valores: {num1 + num2}')
#     case 2:
#         print(f'Resultado da multiplicação dos valores: {num1 * num2}')
#     case _:
#         print('Opção inválida!')

''' 
Conclua o exemplo inserindo: 
    multiplicar, dividir e resto da divisão.
'''
menu=int(input(f'''
               Calculadora - Escolha uma das opções:
               [1]soma
               [2]multiplicação
               [3]divisão
               [4]subtração 
               [5]resto da divisão  
               Opção: '''))
num1 = float(input('Informe um número:'))
num2 = float(input('Informe um número:'))

match menu:
    case 1:
        print(f'Resultado da soma dos valores: {num1 + num2:.2f}')
    case 2:
        print(f'Resultado da multiplicação dos valores: {num1 * num2:.2f}')
    case 3:
        print(f'Resultado da divisão dos valores: {num1 / num2:.2f}')
    case 4:
        print(f'Resultado da subtração dos valores: {num1 - num2:.2f}')
    case 5:
        print(f'Resto da divisão dos valores: {num1 % num2:.2f}')
    case _:
        print('Opção inválida!')


# print('Calculadora 4 Operações Matemáticas')
# #variáveis#
# num1 = input('Informe um número:')
# num2 = input('Informe um número:')


# #condição#
# soma1 = int(num1) + int(num2)
# soma2 = int(num1) - int(num2)
# soma3 = int(num1) * int(num2)
# soma4 = int(num1) / int(num2)

# print(f'Resultado da soma dos valores: {soma1}')
# print(f'Resultado da subtração dos valores: {soma2}')
# print(f'Resultado da multiplicação dos valores: {soma3}')
# print(f'Resultado da divisão dos valores: {soma4}')