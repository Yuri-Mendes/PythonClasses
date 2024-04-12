"""
Operadores Aritméticos e lógicos:

+  Adição           *  Multiplicação
-  Subtração        ** Exponenciação(potência)

/  Divisão
// Retorna o valor inteiro da divisão
%  Retorna o resto da divisão

>   Maior           ==  Igual
<   Menor           !=  Diferente

>=  Maior ou igual
<=  Menor ou igual
=   Atribuição
"""

a = 2
b = 3

print(a + b)   # adição
print(a - b)   # subtrair

print(a * b)   # multiplicar
print(a ** b)  # exp

print(a / b)   # divisão
print(a // b)  # divisão com valor inteiro
print(a % b)   # resto da divisão

print(a > b)   # [a] é maior que [b]?
print(a <= b)  # [a] é menor ou igual [b]?
print(a == b)  # [a] é igual [b]?
print(a != b)  # [a] é diferente de [b]?


#Criar uma soma com dois Valores exibir para o usuario  
num1=100
num2=50
resultado=num1+num2
print(f'O resultado é {resultado}')



#Cálculo de Media com duas notas exibir para o usuario o resultado da média
nota1=10
nota2=9
nota3=9
nota4=10
media=(nota1+nota2+nota3+nota4) / 4
print(f'A média das notas: {media:.2f}')
#:.0f - arrendondar os valores e definir a quantidade de casas decimais

# – Cálculo de aumento de salário
salario=6546.32
percentual=0.10
aumento= salario + (salario*percentual)
print(f'Seu salário será {aumento:.2f}')

salario=6.546
percentual=0.10
aumento= salario + (salario*percentual)
print(f'Seu salário será {aumento:.3f}')