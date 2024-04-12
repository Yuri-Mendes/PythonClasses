"""
Tuplas >>> Tuple

Tuplas não são mutáveis, uma vez criada, permanecerá tal qual durante do o código.
- Aceita assim como as listas, quaisquer tipos de dados.

Sintaxe's
variável = ()
variável = tuple()

Tuplas são definidas por , e não pelo uso de parenteses.

Métodos de adição, remoção, alteração, ordenação em tuplas não existem.

Utilizamos em coleções que não sofrem alterações.
"""


# Criando uma tupla 

#meses = (2,4,5,6,8,11,12)
# meses = ('Março','Junho','Novembro','Dezembro')
# print(meses[0])

# calculo = (2,4,5,6,8,11,12)
# print(calculo[0]*[3])

# meses = ('Março','Junho','Novembro','Dezembro')
# meses[1]='Agosto'
# print(meses)


#Tupla com dados de Meses

meses = ('Março','Junho','Novembro','Dezembro')
print(meses)


#Tupla com dados Dia da semana

dia = ('Terça','Quarta','Quinta','Sexta')
print(dia)


##Tupla com dados de CPF
import collections
cpf = ('66166123094','11493890018','22860923039','62453110047')
print(cpf)
print(max(cpf)) #Max retorna o maior valor dentro da tupla
print(min(cpf)) #Min retorna o menor valor dentro da tupla
print(len(cpf)) #Len retorna quantos elementos tem na tupla
print(cpf.count(1)) #Count retorna quantas vezes apareceu o valor 2 dento da tupla

##Tupla com dados de Codigo de Cliente

cod_cliente = ('1458','1378','5689','1746')
print(cod_cliente)
