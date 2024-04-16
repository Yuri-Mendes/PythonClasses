#Modulo GetPass serve para ocultar uma senha muito usada para login

import getpass

username=input('Digite seu nome de usuário: ')
password=getpass.getpass('Digite sua senha: ')

print(f' usuario: {username}, senha: {password}')
