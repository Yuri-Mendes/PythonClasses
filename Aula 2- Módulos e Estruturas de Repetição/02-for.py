"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
"""
# sintaxe
# for contagem in range(0, 5, 1):
#     print(contagem)

# for contagem in range(2, 10, 2):
#     print(contagem)

'''
Crie um sistema que receba 4 notas 
usar uma variavel soma para acumula as notas e 
calcule a média, ao fim apresente a média e situção
do aluno, sendo:
> 7 aprovado, > 5 em recuperação e < 5 reprovado.
'''
# += para incrementar +1 na variável

soma = 0
for n in range(1,5):
    nota=float(input(f'Digite a {n}ª nota: '))
    soma += nota

media= round(soma / n, 1)
print(f'Média final é: {media}')
if media >=7:
    x = 'Aprovado'
elif media >=5:
    x = 'Em recuperação'
else:
    x = 'Reprovado'
print (f'A média final do aluno é: {media}. O aluno está {x}.')
