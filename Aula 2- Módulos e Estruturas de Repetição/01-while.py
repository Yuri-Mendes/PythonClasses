"""
While >>> Permite que você crie um programa que execulte  repetições(loops) 
diversas vezez dependendo de uma condição.

vezes será repetido.
* Necessário atentar para o critério de parada.(loop infinito)

Sintaxe >>>  while <condição>:
                    bloco
  
"""

#Lógica 
"""
    variavel X que armazena um valor 1
    Enquando X for menor e igual a 3:
    Faça
       
"""
#exemplo

#Contadores - Usado como Incremento da variavel ate  que seja Verdadeiro
contagem = 0 #variável acumuladora
# while contagem <=6:
#     print(contagem)
#     contagem += 1
    # x=x +1 - incremento a cada loop do while até que seja verdadeiro.

#Exemplo

while True:
    resposta = str(input("Digite 'sair' para fechar o programa: "))
    if resposta.lower() == 'sair':
        print('Encerrando o loop.')
        break
    else:
        print('Ok, loop continua.')
    print('Continuando o programa')



