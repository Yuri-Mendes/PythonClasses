"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""

# compras={'alface':0.45,
#          'batata':1.20,
#          'cenoura':7.0,
#          'tomate':8.00,
#          'ovo':10.0}
# print(compras.keys(), compras.values())
# print(compras.values())


# compras={'alface':0.45,
#          'batata':1.20,
#          'cenoura':7.0,
#          'tomate':8.00,
#          'ovo':10.0}
# print(compras)

# dados_cliente={
#     'nome':'renan',
#     'endereco':'rua escola',
#     'telefone':'124579655',
#     'idade':'41'
# }
# dados_cliente['idade']=40
# print(dados_cliente)

#remover item com o pop
# dados_cliente={
#     'nome':'renan',
#     'endereco':'rua escola',
#     'telefone':'124579655',
#     'idade':'41'
# }
# dados_cliente.pop('telefone')
# print(dados_cliente)

compras={'Alface':0.45,
         'Batata':1.20,
         'Cenoura':7.0,
         'Tomate':8.00,
         'Ovo':10.0}

while True:
    produto= input('Digite o nome do produto, fim para terminar:').capitalize()
    if produto == 'fim':
        break
    if produto in compras:
        print(f'Produto: {produto}, Preço R$: {compras[produto]:.2f}')
    else:
        print('\nProduto não encontrado.\n')

# while True:
#     produto= input('Digite o nome do produto, fim para terminar:')
#     if produto == 'fim':
#         break
#     if produto in compras:
#         print(f'Preço {compras[produto]:.2f}')
#     else:
#         print('\nProduto não encontrado.\n')
