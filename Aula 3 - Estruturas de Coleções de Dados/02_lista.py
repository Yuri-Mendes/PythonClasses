"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

"""

#*Criar uma lista de Produtos*
# produtos=['Bacon',10.0,'Ovos',12.0,'Manteiga',8.50,'Pão',10.50]
# print(produtos)

#Acesso ao elementos da lista
# print(produtos[0], produtos[1])
# print(f'O produto escolhido: {produtos[0]}. Preço R$: {produtos[1]}')

"""Fatiamento de itens da Lista"""

#obter os dois primeiro elementos da lista [: indice]
# produtos=['Bacon',10.0,'Ovos',12.0,'Manteiga',8.50,'Pão',10.50]
# print(produtos[:2])


#obter os elementos após o segundo elemento [indice :]
# produtos=['Bacon',10.0,'Ovos',12.0,'Manteiga',8.50,'Pão',10.50]
# print(produtos[4:])


# #Obter Trechos de uma Lista [indice inicial :indice final]
# produtos=['Bacon',10.0,'Ovos',12.0,'Manteiga',8.50,'Pão',10.50]
# print(produtos[-2:])

# produtos=['Bacon',10.0,'Ovos',12.0,'Manteiga',8.50,'Pão',10.50]
# print(produtos[2:4])

# usuario = ['Carlos', 52, 1.71, 'Corretor', True]
# print(usuario[0])
# print(usuario[2])
# print(len(usuario))

# produtos=['Bacon',10.0,'Ovos',12.0,'Manteiga',8.50,'Pão',10.50]
# print(produtos[1])
# print(produtos[3])


"""acessar os elementos de uma  lista usando indice negativo """


#APPENDD >>> Atribui a lista, um elemento por vez
# nomes=['joana','alberto','luis','cristina', 'roberto']
# nomes.capitalize()
# nomes.append('ana')
# print(nomes)

# #INSERT >>> Atribui vários elementos, integrando à lista original.
# nomes.insert(1,'renan')
# print(nomes)

# #POP >>> Remove um valor da lista por índice.
# #nomes.pop(2)
# nomes.pop()
# print(nomes)

# #REMOVE >>> Remove um valor da lista por valor.
# nomes.remove('cristina')
# print(nomes)

# #CLEAR >>> Limpa a lista.
# # nomes.clear()
# # print(nomes)

# #SORT >>> Ordena os dados de uma lista.
# nomes.sort()
# print(nomes)

#REVERSE >>> Inverte a lista.
nomes=['joana','alberto','luis','cristina', 'roberto']
nomes.reverse()
print(nomes)

# Interar os itens de uma lista 
cliente=['joana','alberto','luis','cristina','roberto']
cliente.sort()
for nome in cliente:
    print(nome)

#interando em uma lista e adicionando itens no final da lista
# nomes=[]
# for inter in range(5):
#     nomes.append(str(input('Digite o nome do cliente:')))
#     nomes.sort()
#     print(nomes)

#Funções (Sum,Max,Min,Len,Count,Sort, Reverse)
# numeros=[10,20,30,40,50,60,70,80]
# print(sum(numeros))

# numeros=[10,20,30,40,50,60,70,80]
# print(max(numeros))

# numeros=[10,20,30,40,50,60,70,80]
# print(min(numeros))

# numeros=[10,20,30,40,50,60,70,80]
# print(len(numeros))

# print(numeros.count(10))

# numeros.sort()
# print(numeros)

# numeros.reverse()
# print(numeros)

#Varias listas

# produto1=['maçã',2.50,'pera',3.50]
# produto2=['uva',10.0,'morango',6.00]
# produto3=['leite',5.00,'pao',5.00]

# compras=[produto1, produto2, produto3]
# print(compras)

#juntar listas
# produto1=['maçã',2.50,'pera',3.50]
# produto2=['uva',10.0,'morango',6.00]
# produto3=['leite',5.00,'pao',5.00]

# compras=produto1+produto2
# print(compras)


#interando em uma lista e adicionando itens no final da lista
# carro=['audi','bmw','mercedes']
# for item in carro:
#     print(item)
#     if (item=='bmw'):
#         break