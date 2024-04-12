"""
1 -Vamos iniciar um programa que faça entrada com o usuario que receba:
nome
idade
peso
altura

Retorne o IMC do usuário.

IMC =   Peso
      --------
       Altura²
"""
# ** potencia

# nome=str(input('Digite seu nome:')).capitalize()
# idade=int (input('Digite sua idade:'))
# peso=float (input('Digite seu peso:'))
# altura=float (input('Digite sua altura:'))
# imc= peso / altura**2
# print(f'Seu nome é {nome}\nVocê tem {idade} anos\nVocê pesa {peso} kilos\nSua altura é {altura}')

# print(f'Seu IMC é: {imc:.2f}')


"""
2-Considere um programa que solicite a entrada do nome de uma pessoa e  seu ano de nascimento e apresente
a sua idade usando as variaveis nome, ano_nasc, ano_atual e variável idade para armzenar o calculo da idade.

"""
# import datetime
# nome=str(input('Digite seu nome:')).capitalize()
# ano_nasc=int(input('Digite seu ano de nascimento:'))
# currentDateTime = datetime.datetime.now()
# ano_atual = currentDateTime.date()
# idade= ano_nasc - (ano_atual)
# print(f'Seu nome é \nVocê tem {idade} anos')


# nome=str(input('Digite seu nome:')).capitalize()
# ano_nasc=int(input('Digite seu ano de nascimento:'))
# ano_atual=int(input('Digite o ano atual:'))
# idade= ano_atual - ano_nasc
# print(f'Seu nome é {nome} \nVocê tem {idade} anos')

# import datetime

# currentDateTime = datetime.datetime.now()
# date = currentDateTime.date()
# print(f"Current Year -> {date.year}")

"""
3-O Programa Seguinte deve calcular o salário líquido de um profissionalque trabalhe por hora.
Para tanto é necessário possuir alguns dados básicos, tais como:
valor hora , numero de horas trabalhada no mês , Percentual de Desconto do INSS
Apresentar os resultados do salário bruto do valor descontato e do salário Liquido.      

"""
import datetime
nome=str(input('Digite o nome do colaborador:')).capitalize()
matricula=int(input('Digite o número da matrícula do colaborador:'))
mes=int(input('Digite o mês de referência:'))
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
v_hora=float(input('Informe o valor da hora de trabalho:'))
t_horas=float(input('Informe quantas horas trabalhadas:'))
desconto=float(input('Informe o percentual de desconto do INSS:'))
salario_bruto= v_hora * t_horas
desconto= salario_bruto * (desconto/100)
salario_liquido= salario_bruto - desconto

print(f'Relatório de pagamento \nColaborador: {nome} - {matricula} \nMês referência: {mes} \nTotal de {t_horas} horas trabalhadas:\Valor do desconto do INSS: {desconto}')
print(f'Seu salário bruto é: {salario_bruto}')
print(f'Seu salário liquído é: {salario_liquido}')
print(f'Este relatório foi gerado em {date}')
