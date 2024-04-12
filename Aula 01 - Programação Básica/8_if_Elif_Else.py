"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
    
Exemplo de aplicação: 
"""
# idade=17
# if idade >=18:
#     print(f'Você é maior de idade.')
# else:
#     print(f'Você é menor de idade.')

# Condição simples (IF)
'''
Programa - Verificando Se a idade inserida é maior ou igual a 18
'''
# idade=int(input('Digite sua idade:'))

# if idade < 18:
#     print(f'Você é maior de idade.')

# else:
#     print(f'Você é menor de idade.')

# Condição composta (If/else)
"""Programa - Verificar: Se a idade é maior ou igual a 18 , exibir "Maior Idade" caso contrario
será de Menor Idade """

# idade=int(input('Digite sua idade:'))

# if idade < 18:
#     print(f'Este acesso só é permitido para maiores de 18 anos.')

# else:
#     print(f'Você é maior de 18 anos, seu acesso foi permitido.')


# Condição Aninhada (If/Elif/Else)

"""Programa - Se a idade for maior e igual a 18,"maior idade"
              Se a idade for  igual a 16 "você esta quase lá"
              caso contrário "você é menor de idade"
"""

idade=int(input('Digite sua idade:'))

if idade < 16:
    print(f'Você é menor de idade. Este acesso só é permitido para maiores de 18 anos.')

elif idade <= 17:
    print(f'Você está quase lá, porém seu acesso ainda não está permitido.')

else:
    print(f'Você é maior de 18 anos, seu acesso foi permitido.')


