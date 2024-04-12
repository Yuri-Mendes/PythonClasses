"""1.Uma escola precisa de um software que calcule a 
média de alunos. 
Para isso o software deve receber o nome e três 
notas dos alunos. Com estes dados o software deve imprimir:
| ---------------------------------- | 
| Média	    | Imprimir               | 
| ---------------------------------- | 
| ==10	    | Aprovado com Distinção |
| >=7	    | Aprovado!              |
| >=5   	| Em exame               |
| <5	    | Reprovado              |
| ---------------------------------- | 
"""
print('Calculadora de média de aluno')
nome=str(input('Digite o nome do aluno:')).capitalize()
matricula=int(input('Digite a matrícula do aluno:'))
nota1=float(input('Digite a 1ª nota:'))
nota2=float(input('Digite a 2ª nota:'))
nota3=float(input('Digite a 3ª nota:'))
media= (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f'Aprovado com Distinção')
elif media >= 7:
    print(f'Aprovado!')
elif media >=5:
    print(f'Em exame')
else:
    print(f'Reprovado')
print(f'Média final do aluno {nome}-{matricula}: {media}')

