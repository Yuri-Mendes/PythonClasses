class Professor:
    def __init__(self, nome, cpf, rg):
        self._nome = nome
        self._cpf = cpf
        self._rg = rg

usuario1 = Professor('Leo', 132, 456)
print(usuario1._nome,usuario1._cpf, usuario1._rg)


# class Professor:
#     def __init__(self, nome, cpf, rg):
#         self._nome = nome
#         self.__cpf = cpf
#         self.__rg = rg

#     def getNome(self):
#         return f'{self._nome}'
    
# usuario1 = Professor('Leo', 132, 456)
# print(usuario1._nome,usuario1.__cpf, usuario1.__rg)


# class Aluno:
#     def __init__(self, nome, cpf, matricula):
#         self._nome = nome
#         self.__cpf = cpf
#         self.__matricula = matricula

#     def getNome(self):
#         return f'{self._nome}'
    
# usuario1 = Aluno('Leo', 132, 'A4010')
# print(Aluno.getNome())