import datetime
print('Calculadora de IR')
nome=str(input('Digite seu nome:')).title()
endereco=str(input('Informe seu endereço:')).title()
empresa=str(input('Informe a empresa:')).title()
cargo=str(input('Informe seu cargo:')).title()
salario_bruto=float(input('Digite seu salário bruto:'))
mes=int(input('Digite o mês de referência:'))
c = datetime.datetime.now()

if salario_bruto<=1903.98:
    aliquota=0
    deducao=0
elif salario_bruto<=2826.65:
    aliquota=7.5
    deducao=142.80
elif salario_bruto<=3751.05:
    aliquota=15
    deducao=354.80
elif salario_bruto<=4664.68:
    aliquota=22.5
    deducao=636.13
else:
    aliquota=27.5
    deducao=869.36

ir=(salario_bruto * aliquota / 100) - deducao
salario_liquido= salario_bruto - ir

print('\nCálculo Imposto de Renda')
print(f'Nome: {nome}\n'
      f'Empresa: {empresa}\n'
      f'Cargo: {cargo}\n'
      f'Endereço: {endereco}\n'
      f'Salário Bruto: {salario_bruto}\n'
      f'Imposto de renda: {round(ir, 2)}\n'
      f'Percentual desconto: {aliquota}%\n'
      f'Salário Liquído: {salario_liquido}')
print(f'Relatorio gerado em {c}')

