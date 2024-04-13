
# Com retorno

# com mais de 1 retorno

#calculadora
import math #importar módulo

def soma():
    n1=float(input('Digite o 1º valor: '))
    n2=float(input('Digite o 2º valor: '))
    return n1+n2
def subtracao():
    n1=float(input('Digite o 1º valor: '))
    n2=float(input('Digite o 2º valor: '))
    return n1-n2
def multiplicacao():
    n1=float(input('Digite o 1º valor: '))
    n2=float(input('Digite o 2º valor: '))
    return n1*n2
def divisao():
    n1=float(input('Digite o 1º valor: '))
    n2=float(input('Digite o 2º valor: '))
    return n1/n2
def potencia(): #elevado
    n1=float(input('Digite o 1º valor: '))
    n2=float(input('Digite o 2º valor: '))
def raizquadrada(): #raizquadrada
    n1=float(input('Digite o valor: '))
    return math.sqrt(n1)
def porcentagem(): #porcentagem
    n1=float(input('Digite o valor: '))
    n2=float(input('Digite o percentual: '))
    return n1*(n2/100)
while True:
    escolha=int(input(f'''\nCalculadora - Escolha um opção:\n
                      [1]Para Soma
                      [2]Para Subtração
                      [3]Para Multiplicação
                      [4]Para Divisão
                      [5]Para Potência
                      [6]Para Raiz quadrada
                      [7]Para Porcentagem
                      [8]Fechar
                      '''))
    if escolha == 1:
        print(soma())
    elif escolha == 2:
        print(subtracao())
    elif escolha == 3:
        print(multiplicacao())
    elif escolha == 4:
        print(divisao())
    elif escolha == 5:
        print(potencia())
    elif escolha == 6:
        print(raizquadrada())
    elif escolha == 7:
        print(porcentagem())
    elif escolha == 8:
        print('Encerrando o programa.')
        break
    else:
        print('\nOpção inválida.')
        break

    
  
        
        


    
    