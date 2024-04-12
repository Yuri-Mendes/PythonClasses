"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:


| Menor que 18.5      | Abaixo do peso       |
| >=18.5  and <= 24.9   | Peso Normal          |
| >= 25.0 and <= 29.9   | Excesso de peso      |
| >=30.0  and  <=34.9   | Obesidade classe I   |
| >=35.0  and  <=39.9   | Obesidade classe II  |
|caso contrário sera  | Obesidade classe III |

"""
print('Calculadora de IMC')

peso=int(input('Informe seu peso:'))
altura=float(input('Informe sua altura:'))
imc=peso / altura**2
print(f'Seu IMC é: {imc:.2f}')
if imc<18.5:
    resultado = 'Abaixo do peso.'
elif imc>=18.5  and imc<= 24.9:
    resultado = 'Peso Normal.'
elif imc>=25.0  and  imc<=29.9:
    resultado = 'Sobrepeso.'
elif imc>=30.0  and  imc<=34.9:
    resultado = 'Obesidade classe I.'
elif imc>=35.0  and  imc<=39.9:
    resultado = 'Obesidade classe II.'
else:
    resultado = 'Obesidade classe III.'
print(f'Resultado: {resultado}')

