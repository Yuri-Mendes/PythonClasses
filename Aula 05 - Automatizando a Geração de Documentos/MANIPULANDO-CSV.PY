#ARQUIVO CSS

# import csv
# dados=[
#     ['Maria','maria@exemplo.com'],
#     ['Joana','joana@exemplo.com'],
#     ['Henrique','henrique@exemplo.com'],
#     ['Caio','caio@exemplo.com']
# ]
# with open('contatos.csv', 'w', newline='') as arquivo:
#     escrever=csv.writer(arquivo)
#     for linha in dados:
#         escrever.writerow(linha)

import csv
with open('contatos.csv', 'r') as arquivo:
    lendo=csv.reader(arquivo)
    for linha in lendo:
        print(linha[0:1]) #[1:2] quais posições retornar
        
#Este código irá abrir o arquivo, ler cada linha e, 
#em seguida, imprimir cada linha para o console.
