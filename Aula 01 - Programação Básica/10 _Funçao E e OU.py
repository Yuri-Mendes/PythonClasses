"""Função And(E)"""

#E (and) - cria a condição lógica
#para retornar o resultado verdadeiro todo o teste lógico deve ser verdadeiro
# v v = v
# v f = f
# f v = f
# f f = f

"""Situação
Se a média for Maior e igual a 7 E média Menor e igual 10
"Aluno Aprovado"

Se a media for Maior e Igual a 5 E media menor que 7
"Aluno de Recuperação"

se a media for maior e igual que 0 e media < 5
"aluno reprovado"

senão "Média invalida"

"""
# print('Calculadora de média de aluno')
# nome=str(input('Digite o nome do aluno:')).capitalize()
# matricula=int(input('Digite a matrícula do aluno:'))
# nota1=float(input('Digite a 1ª nota:'))
# nota2=float(input('Digite a 2ª nota:'))
# nota3=float(input('Digite a 3ª nota:'))
# media=(nota1 + nota2 + nota3)/3

# if media >=7 and media<=10:
#     print(f'Aluno Aprovado')
# elif media >=5 and media<7:
#     print(f'Aluno em Recuperação')
# elif media >=0 and media<5:
#     print(f'Aluno Reprovado')
# else:
#     print(f'Média inválida')
# print(f'Média final do aluno {nome}-{matricula}: {media:.2f}')


""" Usando o Comando OR (ou)"""

""" 
lucas = 21
carolina=18

se idade de Lucas for >=18 ou idade carolina for >=18
então "Pelo menos um dos dois são de maior Idade"

"""
# Ou
# v v = v
# v f = v
# f v = v
# f f = f

lucas=int(input('Digite a idade de Lucas:'))
carolina=int(input('Digite a idade de Carolina:'))

if lucas >=18 or carolina >=21:
    print(f'Pelo menos um dos é maior de idade')
else:
    print('Menor de idade')