print('***Jogo de Adivinhação***')
import random as rd

numero=rd.randint(1,60)

tentativas=0
chances=10

print('Este é um sistema de loteria, teste sua sorte')
print(f'Escolha um número entre 1 e 60. Você tem {chances} tentativas.')

while tentativas < chances:
    aposta = int(input('Informe o número do seu palpite: '))
    tentativas += 1

    if aposta < numero:
        print(f'Não foi dessa vez, tente outro número.\n')
    elif aposta > numero:
        print(f'Ainda não foi dessa vez, continue tentando.\n')
    else:
        print(f'\Parabéns, você acertou o número secreto e ganhou o prêmio máximo. Número sorteado {numero}.')
        print(f'Total de tentativas usadas:{tentativas}')
        break
    
    if tentativas == chances and aposta !=numero:
        print(f'Você não tem mais tentativas.\n'
              f'Este foi o número sorteado: {numero}.\n')